#!/bin/python

import boto.ec2
import datetime
from dateutil import parser

conn = boto.connect_ec2()
reservations = conn.get_all_instances()

print('\n\nInstances which are launched and running from 30 to 365 days-\n\n')

for r in reservations:
    for instance in r.instances:
        if instance.state == "running":
            launchtime = parser.parse(instance.launch_time)
            launchtime_naive = launchtime.replace(tzinfo=None)
            after = datetime.datetime.utcnow() + datetime.timedelta(days=-30)
            before = datetime.datetime.utcnow() + datetime.timedelta(days=-365)
            if (launchtime_naive < after) and (launchtime_naive > before):
                print(instance.id)

print('\n\nInstances which are launched and running from 15 to 30 days-\n\n')

for r in reservations:
    for instance in r.instances:
        if instance.state == "running":
            launchtime = parser.parse(instance.launch_time)
            launchtime_naive = launchtime.replace(tzinfo=None)
            after1 = datetime.datetime.utcnow() + datetime.timedelta(days=-15)
            before1 = datetime.datetime.utcnow() + datetime.timedelta(days=-30)
            if (launchtime_naive < after1) and (launchtime_naive > before1):
                print(instance.id)

print('\n\nInstances which are launched and running from 7 to 15 days-\n\n')

for r in reservations:
    for instance in r.instances:
        if instance.state == "running":
            launchtime = parser.parse(instance.launch_time)
            launchtime_naive = launchtime.replace(tzinfo=None)
            after2 = datetime.datetime.utcnow() + datetime.timedelta(days=-7)
            before2 = datetime.datetime.utcnow() + datetime.timedelta(days=-15)
            if (launchtime_naive < after2) and (launchtime_naive > before2):
                print(instance.id)
