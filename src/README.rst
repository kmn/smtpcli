======================================
`smtpcli` is SMTP Client tool.
======================================

This command line tool for SMTP client.

Requirements
------------

* Python 2.7 or later.


Setup
-----

Case: Github

::

   $ git clone https://github.com/kmn/smtpcli
   $ cd smtpcli
   $ sudo python setup.py install
   $ cp sample/smtpcli.conf.sample $HOME/.smtpcli.conf
 
   and edit $HOME/.smtpcli.conf

Case: Pypi

::
   $ sudo pip install smtpcli
   $ cp sample/smtpcli.conf.sample $HOME/.smtpcli.conf
 
   and edit $HOME/.smtpcli.conf

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
   $ echo "Hello, world!" > msg.txt
   $ smtpcli --to user007@example.org  --subject "from 001 to 007" \
     --file msg.txt

   To: user007@example.org
   Subject: from 001 to 007
   Body: Hello, world!

   Send this email? [y/N] 


History
-------

0.3 (2012-09-16)
~~~~~~~~~~~~~~~~
* fix minor bugs

0.2 (2012-09-16)
~~~~~~~~~~~~~~~~
* fix minor bugs

0.1 (2012-09-16)
~~~~~~~~~~~~~~~~
* modify setup.py

0.0 (2012-06)
~~~~~~~~~~~~~~~~
* first release


See also
--------

* `RFC 821  <http://tools.ietf.org/html/rfc821.html>`_
* `RFC 1896 <http://tools.ietf.org/html/rfc1869.html>`_
