#!/usr/bin/python3

import re
import sys

def parse(file):
	insub=0
	linen=0
	texst=0
	fc=[line.strip() for line in open(file, "r")]
	print("<parser> In file", file, ':')
	for l in fc:
		if re.match('^\.[Ss][Uu][Bb][Cc][Kk][Tt]', l)!=None:
			insub=1
			continue
		elif re.match('^\.[Ee][Nn][Dd]', l)!=None and insub:
			insub=0
			continue
		if not insub:
			m=re.match('(^[mM]\S*).*([wW]=\S*).*([lL]=\d[uU])', l)
			if m!=None:
				print("\t",m.groups()[0],m.groups()[1],m.groups()[2])
				texst=1
		linen+=1
	if not texst:
		print("\t No such transistors")

def arghandler(arg):
	try:
		f=open(arg, "r")
	except FileNotFoundError:
		print("<arghdl> W1:",arg, "- no such file")
		return
	except IsADirectoryError:
		print("<arghdl> W2:",arg,"is a directory")
		return
	except PermissionError:
		print("<arghdl> W3:",arg, "- unable to read")
		return
	if re.match('.*\.sp$', arg)==None:
		print("<arghdl> W4:",arg,"is not an .sp file")
		return
	parse(arg)
	return

args=sys.argv[1:]
if args:
	for arg in args:
		arghandler(arg)
else:
	arg=input("Type filename: ")
	arghandler(arg)

