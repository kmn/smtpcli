#!/usr/bin/python -S
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.Header import Header
import ConfigParser
from optparse import OptionParser


# Set config
config_file = os.environ.get('HOME') + '/.smtpcli.conf'

if os.path.isfile(config_file):
    smtpserver, port, encoding, from_addr, password =   False, False, False, False, False
else: 
    print '''
    Error: $HOME/.smtpcli.conf does not exist.
    Usage: cp smtpcli/smtpcli.conf $HOME/.smtpcli.conf
    '''
    sys.exit()
conf = ConfigParser.SafeConfigParser()
conf.read(config_file)
smtpserver = conf.get('smtpcli', 'smtp-server') 
port        = conf.get('smtpcli', 'port')
encoding    = conf.get('smtpcli', 'encoding')
from_addr   = conf.get('smtpcli', 'mailaddress')
password    = conf.get('smtpcli', 'password')


to_addr      = False
subject      = False
body         = False
file         = False

#Define sub-command and command line options

import argparse
from __init__ import __version__

parser = argparse.ArgumentParser(description='usage')
parser.add_argument('-v', '--version', action='version',
                       version=__version__)
parser.add_argument('-t', '--to', metavar='dest_address', help='destination mail address', required=True)
parser.add_argument('-s', '--subject', metavar='subject', help='email subject', required=True)
parser.add_argument('-f', '--file', metavar='filename', help='the file containing email body',required=True, type=argparse.FileType('r'))
#parser.add_argument('--no-confirm', metavar='no-confirm', help='no confirm')
args = parser.parse_args()

to_addr = args.to
subject = args.subject
body = args.file.read()


def create_message(from_addr, to_addr, subject, body, encoding):
    '''
    create MIME document like 'text/plain; charset="encoding"'
    '''
    msg = MIMEText(body, 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From']    = from_addr
    msg['To']      = to_addr
    msg['Date']    = formatdate()
    return msg

def send_via_smtp(from_addr, to_addr, msg):
    '''
    send mail via smtp
    '''
    ss = smtplib.SMTP(smtpserver, port)
    ss.starttls()
    ss.login(from_addr, password)
    ss.sendmail(from_addr, to_addr, msg.as_string())
    ss.close

def query_yes_no(question, default="no"):
    '''Ask a yes/no question via row_input() and return their answer.
    "questin" is a string that is presented to the user.
    "default" is the presumed answer if the user just hit <Enter>.
        It must be "yes", "no"(default)  or None (meaning an
        answer is required of the user).

    " The "anwer" return value is one of "yes" or "no".
    '''
    valid = {"yes":True,  "y":True, "ye":True,
             "no":False,  "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                "(or 'y' or 'n').\n")

def send_confirm():
    print "To: " + to_addr
    print "Subject: " + subject
    print "Body: " + body
    if query_yes_no("Send this email?") == False:
        sys.exit()


def main():
    send_confirm()
    msg = create_message(from_addr, to_addr, subject, body, encoding)
    send_via_smtp(from_addr, to_addr, msg)
    print("Sent email, Successfully")

if __name__ == '__main__':
    main()
