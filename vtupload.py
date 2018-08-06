#!/usr/bin/env python
from sys import argv
from vtapi import Public as vt

if __name__ == '__main__':
	result = vt.check_file(argv[0])
	if result != 0:
		print('INFECTED')
		