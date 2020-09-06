#!/bin/python

import datetime
import boto
from dateutil import parser

connection = boto.connect_ec2()

AMIs = connection.get_all_images(filters={'owner-id': 194014789460})

print('\n\n'+'AMIs older than 180 days'+'\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-180)

for ami in AMIs:
    if parser.parse(ami.creationDate).date() < timeLimit.date():
        print(ami.id)

print('\n\n' + 'AMIs older than 90 days' + '\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-90)

for ami in AMIs:
    if parser.parse(ami.creationDate).date() < timeLimit.date():
        print(ami.id)

print('\n\n' + 'AMIs older than 30 days' + '\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-30)

for ami in AMIs:
    if parser.parse(ami.creationDate).date() < timeLimit.date():
        print(ami.id)

print('\n\n' + 'AMIs older than 15 days' + '\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-15)

for ami in AMIs:
    if parser.parse(ami.creationDate).date() < timeLimit.date():
        print(ami.id)

print('------------------------------')
