#!/bin/python

import datetime
import boto
from dateutil import parser

connection = boto.connect_ec2()

eIPs = connection.get_all_addresses()

print('\n\n'+'Un-attached Elastic IPs'+'\n')

for eIP in eIPs:
	if eIP.association_id is None:
		print(eIP.public_ip+' : '+eIP.allocation_id)