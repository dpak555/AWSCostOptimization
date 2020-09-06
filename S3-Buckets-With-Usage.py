#!/bin/python

import boto

s3 = boto.connect_s3()

bucket_list = [i.name for i in s3.get_all_buckets()]

print('\n\n'+'S3 buckets with usage:-'+'\n')

for bucket_name in bucket_list:

	bucket = s3.lookup(bucket_name)
	total_bytes = 0
	n = 0
	for key in bucket:
		total_bytes += key.size
		n += 1
		if n % 2000 == 0:
			print(n)
	total_kbs = total_bytes/1024

	print("%s: %.3f KB, %i objects" % (bucket_name, total_kbs, n))