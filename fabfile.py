#
# This is a fabric automation file that can be used to upload the recipies
# contained in this repo to a remote node, and then run chef-solo on this node.
# Usage:
#     fab -H 123.456.789.0 -u root install_sentry
#

from fabric.api import run, sudo, put
from fabric.contrib.project import rsync_project

def host_type():
    run('uname -s')

def sync_cookbooks():
    rsync_project(remote_dir='/var/chef/cookbooks/', local_dir='chef/cookbooks/')

def sync_roles():
    rsync_project(remote_dir='/var/chef/roles/', local_dir='chef/roles/')

def sync_solo_nodes():
    rsync_project(remote_dir='/var/chef/solo-nodes/', local_dir='chef/solo-nodes/')

def sync_data_bags():
    rsync_project(remote_dir='/var/chef/data_bags/', local_dir='chef/data_bags/')

def sync_chef():
    sync_cookbooks()
    sync_roles()
    sync_data_bags()
    sync_solo_nodes()

def sync_chef_solo_config():
    put(local_path='solo.rb', remote_path='/etc/chef/solo.rb')

def install_sentry():
    sync_chef()
    sync_chef_solo_config()
    sudo('chef-solo -j /var/chef/solo-nodes/sentry-node-solo.json')

