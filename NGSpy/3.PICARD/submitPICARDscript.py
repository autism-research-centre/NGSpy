#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
#indir =os.path.dirname("/mnt/DATA/home4/arc/hb493/GF7/output/b37/BWAMEM/")
#outdir = os.path.dirname("/mnt/DATA/home4/arc/hb493/GF7/output/b37/BWAMEM/PICARD/")

indir = os.path.dirname("/mnt/b2/home4/arc/hb493/Rimma_fastq/PICARD/input/")
outdir = os.path.dirname("/mnt/b2/home4/arc/hb493/Rimma_fastq/PICARD/output/")
bnlist=[]
r=[]
# identify mapped.sorted.bam files
for file in os.listdir(indir):
	# save the basename  and ending	
	fbasename = file.split(".QC.MAP.s.m.bam", 1)[0]
	nn  =  fbasename + ".QC.MAP.s.m.bam"
	if (fbasename!=file):
		if  (nn == file):
			bnlist.append(fbasename)
			r.append(indir + "/" + fbasename + ".QC.MAP.s.m.bam")


for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python /mnt/DATA/home4/arc/hb493/scripts/PICARDscript.py " + bnlist[i] + " " + r[i] + " " + outdir + "\""
	print "sbatch --partition=LONG /mnt/DATA/home4/arc/hb493/bin/submit_sbatch3.sh"
	print "export SBATCH_CMD=\"\""

#	print ("python BOWTIEscript.py " + bnlist[i] + " " + r1[i] + " " + r2[i])


