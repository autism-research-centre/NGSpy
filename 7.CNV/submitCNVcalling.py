#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("path/indir") #output dir from the GATK step
outdir = os.path.dirname("path/outdir")



bnlist=[]
r=[]
# identify mapped.sorted.bam files
for file in os.listdir(indir):
	
	# save the basename  and ending	
	fbasename = file.split(".QC.MAP.s.MDup.RGr.BRec.IReal.bam", 1)[0]
	nn  =  fbasename + ".QC.MAP.s.MDup.RGr.BRec.IReal.bam"
	if (fbasename!=file):
		if  (nn == file):
			bnlist.append(fbasename)
			r.append(indir + "/" + fbasename + ".QC.MAP.s.MDup.RGr.BRec.IReal.bam")


for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python CNVnatorScript.py " + bnlist[i] + " " + r[i] + " " + outdir + "\""
	print "sbatch --partition=1604 submit_sbatch12.sh"
	print "export SBATCH_CMD=\"\""
