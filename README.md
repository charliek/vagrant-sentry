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

A start of this is done using [fabric]. To start navigate to this directory. Note that currently there is no firewall
setup in this recipe so please consider adding this before using.

Clone it from github

$ `git clone git://github.com/charliek/vagrant-sentry.git`

$ `cd vagrant-sentry`

Currently you need to [install chef][chef_install] on the remote box manually, but I hope to automate this in the future. You will also
need to [install fabric][fab_install] locally which will be used to do the automation.

Execute the fabric file to sync the cookbooks and run chef solo. Note you must substitute the host name with the actual host name.

$ `fab -H 123.456.789.0 -u root install_sentry`

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
