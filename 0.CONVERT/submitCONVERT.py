#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("path/indir")
outdir = os.path.dirname("/path/outdir")

# This will:
#     - Identify the bam files in the input folder
#     - Generate a list of bam files to be processed.
#     - Generate a list with the basename (ID name of the sample) 

bnlist=[]
r=[]
# identify mapped.sorted.bam files
for file in os.listdir(indir):
	# save the basename  and ending	
	fbasename = file.split(".bam", 1)[0]
	nn  =  fbasename + ".bam"
	if (fbasename!=file):
		if  (nn == file):
			bnlist.append(fbasename)
			r.append(indir + "/" + fbasename + ".bam")

# Run CONVERTscript.py parallely for each file
for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python CONVERTscript.py " + bnlist[i] + " " + r[i] + " " + outdir + "\""
	print "sbatch --partition=LONG submit_sbatch0.sh"
	print "export SBATCH_CMD=\"\""




