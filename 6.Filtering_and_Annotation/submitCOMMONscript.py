#usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("path/indir") #output dir from FILTER script
outdir = os.path.dirname("path/outdir")


bnlist=[]
r=[]
# identify mapped.sorted.bam files
for file in os.listdir(indir):
	# save the basename  and ending	
	fbasename = file.split(".filtered.vcf", 1)[0]
	nn  =  fbasename + ".filtered.vcf"
	if (fbasename!=file):
		if  (nn == file):
			bnlist.append(fbasename)
			r.append(indir + "/" + fbasename + ".filtered.vcf")


for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python COMMONscript.py " + bnlist[i] + " " + r[i] +  " " + outdir + "\""
	print "sbatch --partition=LONG submit_sbatch13.sh"
	print "export SBATCH_CMD=\"\""

#	print ("python CONVERTscript.py " + bnlist[i] + " " + r[i] + " " + outdir)

