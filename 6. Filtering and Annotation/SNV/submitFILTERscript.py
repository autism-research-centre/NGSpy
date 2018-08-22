#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("path/indir") #output dir from VC/GATKHC
outdir = os.path.dirname("path/outdir")


bnlist=[]
r=[]
# identify vcf files
for file in os.listdir(indir):
	# save the basename  and ending	
	fbasename = file.split(".GATK.vcf", 1)[0]
	nn  =  fbasename + ".GATK.vcf"
	if (fbasename!=file):
		if  (nn == file):
			bnlist.append(fbasename)
			r.append(indir + "/" + fbasename + ".GATK.vcf")


for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python FILTERscript.py " + bnlist[i] + " " + r[i] + " " + outdir + "\""
	print "sbatch --partition=LONG submit_sbatch8.sh"
	print "export SBATCH_CMD=\"\""
	



