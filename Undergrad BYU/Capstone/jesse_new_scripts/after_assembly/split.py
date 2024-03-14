#!/usr/bin/env python

import os
import sys

arguments = sys.argv

filein = arguments[1]
delim=arguments[2]
locuslist = []
count = 0

inputopen = open(filein, "r")
line = inputopen.readline()
while line:
	if line[0] == ">":
		linesplit = line.strip(">").strip().split(delim)
		locus = linesplit[0]
		locuslist.append(locus)
		line = inputopen.readline()
	else:
		line = inputopen.readline()

inputopen.close()

locuslist = set(locuslist)
locuslist = list(locuslist)

count_lists = [[] for i in range(0, len(locuslist))]

inputopen = open(filein, "r")
line = inputopen.readline()
while line:
	if line[0] == ">":
		linesplit = line.strip(">").strip().split(delim)
		locus = linesplit[0]
		location = locuslist.index(locus)
		count_lists[location].append(count)
		count = count + 1
		count_lists[location].append(count)
		count = count + 1
		line = inputopen.readline()
	else:
		line = inputopen.readline()

inputopen.close()
inputopen = open(filein, "r")
lines = inputopen.readlines()
count = 0
for locus in locuslist:
	outfile = open(locus + ".fa", "w")
	for linenumber in count_lists[count]:
		outfile.write(lines[linenumber])
	count = count + 1
	outfile.close()

inputopen.close()
	
