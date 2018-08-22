#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders



indir =os.path.dirname("path/indir") # PICARD output dir
outdir = os.path.dirname("path/outdir") 




bnlist=[]
r=[]
# identify mapped.sorted.bam files
for file in os.listdir(indir):
	# save the basename  and ending	
	fbasename = file.split(".QC.MAP.s.MDup.RGr.bam", 1)[0]
	nn  =  fbasename + ".QC.MAP.s.MDup.RGr.bam"
	if (fbasename!=file):
		if  (nn == file):
			bnlist.append(fbasename)
			r.append(indir + "/" + fbasename + ".QC.MAP.s.MDup.RGr.bam")


for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python GATKscript.py " + bnlist[i] + " " + r[i] + " " + outdir + "\""
	print "sbatch --partition=LONG submit_sbatch4.sh"
	print "export SBATCH_CMD=\"\""

#	print ("python GATKscript.py " + bnlist[i] + " " + r1[i] + " " + r2[i])


