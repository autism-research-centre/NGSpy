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
f2=sys.argv[3]
outdir = sys.argv[4]

# STEP 1 : DISCARDING THE HEADER
dico = {}

outcom = outdir + "/" + basename + ".common.vcf"
outnocom = outdir + "/" + basename + ".no_common.vcf" 
outc= open(outcom, 'a')
outnoc = open(outnocom, 'a')

#creates a dictionary with f2 entries
with open(f2, 'r') as f2o:
	for line in f2o:
		line = line.replace("\n","")
		if(line.find("#")==0):
			pass
		else:
			array=line.split("\t")
			elements = array[0] + " " + array[1] + " " + array[3] + " " + array[4]
			dico[elements] = line

#selects and writes in file lines not found in the dictionary
with open(f1, 'r') as f1o:
	for line in f1o:
		line = line.replace("\n","")
		if(line.find("#")==0):
			outc.write(line + "\n")
			outnoc.write(line + "\n")
			
		else:
			array2=line.split("\t")
			elem2 = array2[0] + " " + array2[1] + " " + array2[3] + " " + array2[4] 
			if (dico.has_key(elem2)):
				outc.write(line + "\n")			
			else:
				outnoc.write(line + "\n")







