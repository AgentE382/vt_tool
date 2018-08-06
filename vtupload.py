#!/usr/bin/env python
from sys import argv
from vtapi import Public

if __name__ == '__main__':
	vt = Public(api_key ='<change this to yours until I implement the key parameter and per-user saved settings>')

	result = vt.check_file(argv[0])
	if result != 0:
		print('INFECTED')
