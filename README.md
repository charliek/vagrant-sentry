Overview
--------

Very early prototype chef setup to get sentry up and running in [vagrant].

* [Sentry hosted version][sentry_hosted]
* [Sentry github source][sentry_source]
* [Sentry documentation][sentry_docs]

Vagrant Setup
-------------

This is rough but it does work to run it locally. To get this working you need to:

Clone it from github

$ `git clone git://github.com/charliek/vagrant-sentry.git`

If you are on a 1.1.x vagrant verison:

$ `cd vagrant-sentry/vagrant/1.1.x`

If you are on a 1.0.x vagrant verison:

$ `cd vagrant-sentry/vagrant/1.0.x`

Start the image:

$ `vagrant up`

Login to the image and create you super users by executing the below command and following the directions:

```
$ vagrant ssh
$ /www/sentry/bin/sentry --config=/etc/sentry.conf.py createsuperuser
$ exit
```

Now you can [login][vagrant_login] with the username and password you setup when the create user script was run.

Setup Using Chef Solo
---------------------

Only tested on Ubuntu 12.04

Included is a [fabric] file that can be used to install chef, sync the chef cookbooks, and run chef solo.
To start navigate to this directory. Before using something like this in production you should make sure
you understand what it is doing. There is till work to be done to make this production ready. Note that
running the included script will redo any firewall rules to only allow incoming connections on 22 and 80.

Clone it from github

$ `git clone git://github.com/charliek/vagrant-sentry.git`

$ `cd vagrant-sentry`

[Install fabric][fab_install] on your local machine if it is not already in place.

On your remote server make sure you have a recent version of chef 10.x.x installed. Currently this recipe
will not work on chef 11.x.x, but hopefully soon. If you don't have chef installed on your server you can
easily install it by executing (Note you must substitute your host name):

$ `fab -H 123.456.789.0 -u root install_chef`

To sync the chef files and execute chef solo run the below command (Note you must substitute your host name):

$ `fab -H 123.456.789.0 -u root install_sentry`

If you don't see any errors you should not see sentry running on port 80.

[vagrant]: http://www.vagrantup.com/
[vagrant_login]: http://192.168.33.11:9000/login/
[sentry_docs]: http://sentry.readthedocs.org/en/latest/
[sentry_hosted]: https://www.getsentry.com
[sentry_source]: https://github.com/getsentry/sentry
[fabric]: http://docs.fabfile.org/en/1.6/#installation
[fab_install]: http://docs.fabfile.org/en/1.6/#installation
[chef_install]: http://stackful-dev.com/three-ways-to-get-chef-chef-solo-installed-on-your-server.html

Disclaimer
----------

Note that this initial version uses clear weak passwords, and I have not setup queues or redis for better caching at this time. Also it could use more work organizing things a bit more logically.
