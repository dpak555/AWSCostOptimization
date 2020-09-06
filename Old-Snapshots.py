#!/bin/python

import datetime
import boto
from dateutil import parser

connection = boto.connect_ec2()
snapshotsID = connection.get_all_snapshots(filters={'owner-id': 194014789460})

print('\n\n'+'Snapshots older than 30 days'+'\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-30)

for sID in snapshotsID:
    if parser.parse(sID.start_time).date() < timeLimit.date():
        print(sID)

print('\n\n' + 'Snapshots older than 15 days' + '\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-15)

for sID in snapshotsID:
    if parser.parse(sID.start_time).date() < timeLimit.date():
        print(sID)

print('\n\n' + 'Snapshots older than 7 days' + '\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-7)

for sID in snapshotsID:
    if parser.parse(sID.start_time).date() < timeLimit.date():
        print(sID)

print('----------------------------------------------------------------------')
