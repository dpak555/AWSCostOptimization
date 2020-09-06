#!/bin/python

import datetime
import boto
from dateutil import parser

connection = boto.connect_ec2()

volumes = connection.get_all_volumes()

print('\n\n'+'Unused Volumes created before 15 days'+'\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-15)

for volume in volumes:
    if parser.parse(volume.create_time).date() < timeLimit.date():
        if volume.status == 'available':
            print(volume.id)


print('\n\n'+'Unused Volumes created before 30 days'+'\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-30)

for volume in volumes:
    if parser.parse(volume.create_time).date() < timeLimit.date():
        if volume.status == 'available':
            print(volume.id)


print('\n\n'+'Unused Volumes created before 60 days'+'\n\n')

timeLimit = datetime.datetime.now() + datetime.timedelta(days=-60)

for volume in volumes:
    if parser.parse(volume.create_time).date() < timeLimit.date():
        if volume.status == 'available':
            print(volume.id)

