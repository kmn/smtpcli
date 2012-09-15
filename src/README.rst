======================================
`smtpcli` is SMTP Client tool.
======================================

This command line tool for SMTP client.

Requirements
------------

* Python 2.7 or later.


Setup
-----
::

   $ git clone https://github.com/kmn/smtpcli
   $ cd smtp
   $ sudo python setup.py install

   
History
-------

0.1 (2012-09)
~~~~~~~~~~~~~~~~
* first release


Usage
-----

Setting the configuration file ($HOME/.smtpcli.conf)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An alternative method of command options that use the config file.
Copy examples/.smtpcli.conf.sample to `$HOME/.smtpcli.conf`. `password` key to set password in plain text.
::

   # 
   [smtpcli]
   smtp-server  = smtp.exmple.org
   port         = 25
   encoding     = ISO-2022-JP
   mailaddress  = user001@exmple.org
   password     = user001pw

Sending mail
~~~~~~~~~~~~~~~~~~~~
::

   $ smtpcli --to user007@example.org  --title "from 001 to 007" \
   --contents-file msg.txt
   true

Contribute
----------

Firstly copy pre-commit hook script.
::

   $ cp -f utils/pre-commit.txt .git/hooks/pre-commit

Next install python2.7 later, and nosetests. Below in Debian GNU/Linux Sid system,
::

   $ sudo apt-get install python python-nose

Then checkout 'devel' branch for development, commit your changes. Before pull request, execute git rebase.


See also
--------

* `RFC 821  <http://tools.ietf.org/html/rfc821.html>`_
* `RFC 1896 <http://tools.ietf.org/html/rfc1869.html>`_
