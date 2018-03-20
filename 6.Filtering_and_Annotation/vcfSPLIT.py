#!/usr/local/bin/python

import os
import sys
import os.path

import numpy

# Take arguments

if len(sys.argv)<>5:
	print("Error: wrong number of arguments")
basename = sys.argv[1]
f1=sys.argv[2]
outdir = sys.argv[3]

# STEP 1 : DISCARDING THE HEADER


out = outdir + "/" + basename + ".split.vcf"
outc= open(out, 'a')


#creates a dictionary with f2 entries
with open(f2, 'r') as f2o:
	for line in f2o:
		line = line.replace("\n","")
		if(line.find("#")==0):
			outc.write(line + "\n")
		else:
			array=line.split("\t")
			alt = array[4]
			if(length(alt.split(","))>1):
				alt2 = alt.split(",")
				array1 = array
				array2 = array
				array1[4] = alt[0]
				outc.write(print('\t'.join(array1))+ "\n")
				array2[4] = alt[1]
				outc.write(print('\t'.join(array2))+ "\n")
			else:
				outc.write(line + "\n")







