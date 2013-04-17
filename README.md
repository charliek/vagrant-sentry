Overview
--------

Very early prototype chef setup to get sentry up and running in vagrant.

Sentry hosted version:

https://www.getsentry.com

Sentry github source:

https://github.com/getsentry/sentry

Sentry documentation:

http://sentry.readthedocs.org/en/latest/

Setup
-----

This is rough but it does work to run it locally. To get this working you need to:

Clone it from github

$ `git clone git://github.com/charliek/vagrant-sentry.git`

Change into the directory with the vagrant file:

$ `cd vagrant-sentry/vagrant/1.1.x`

Start the image:

$ `vagrant up`

Login to the image and create you super users by executing the below command and following the directions:

```
$ vagrant ssh
$ /www/sentry/bin/sentry --config=/etc/sentry.conf.py createsuperuser
$ exit
```

Now you can visit http://192.168.33.11:9000/login/ and login with the username and password you setup when the create user script was run.

Disclaimer
----------

Note that this initial version uses clear weak passwords, and I have not setup queues or redis for better caching at this time. Also it could use more work organizing things a bit more logically.
