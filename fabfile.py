#
# This is a fabric automation file that can be used to upload the recipies
# contained in this repo to a remote node, and then run chef-solo on this node.
# Usage:
#     fab -H 123.456.789.0 -u root install_sentry
#

from fabric.api import run, sudo, put, task
from fabric.contrib.project import rsync_project


CHEF_VERSION = '10.24.0'

@task
def install_chef(latest=False):
    """
    Install chef-solo on the server
    """
    sudo('apt-get update', pty=True)
    sudo('apt-get install -y emacs23-nox ruby1.9.1 ruby1.9.1-dev build-essential', pty=True)

    if latest:
        sudo('gem1.9.1 install --no-ri --no-rdoc chef', pty=True)
    else:
        sudo('gem1.9.1 install --no-ri --no-rdoc --version {0} chef'.format(CHEF_VERSION), pty=True)


def sync_cookbooks():
    sudo('mkdir -p /var/chef/cookbooks')
    rsync_project(remote_dir='/var/chef/cookbooks/', local_dir='chef/cookbooks/')

def sync_roles():
    sudo('mkdir -p /var/chef/roles')
    rsync_project(remote_dir='/var/chef/roles/', local_dir='chef/roles/')

def sync_solo_nodes():
    sudo('mkdir -p /var/chef/solo-nodes')
    rsync_project(remote_dir='/var/chef/solo-nodes/', local_dir='chef/solo-nodes/')

def sync_data_bags():
    sudo('mkdir -p /var/chef/data_bags')
    rsync_project(remote_dir='/var/chef/data_bags/', local_dir='chef/data_bags/')

def sync_chef():
    sync_cookbooks()
    sync_roles()
    sync_data_bags()
    sync_solo_nodes()

@task
def sync_chef_solo_config():
    sudo('mkdir -p /etc/chef')
    put(local_path='solo.rb', remote_path='/etc/chef/solo.rb')

@task
def install_sentry():
    sync_chef()
    sync_chef_solo_config()
    sudo('chef-solo -j /var/chef/solo-nodes/sentry-node-solo.json')

