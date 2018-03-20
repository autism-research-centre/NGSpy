#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("/mnt/DATA/home4/arc/hb493/GF12/output/BWAMEM/PICARD/")
outdir = os.path.dirname("/mnt/DATA/home4/arc/hb493/GF12/output/VC/VARSCAN/")
outdir2 = os.path.dirname("/mnt/DATA/home4/arc/hb493/GF12/output/VC/GATK/")

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
	print "export SBATCH_CMD=\"python /mnt/DATA/home4/arc/hb493/scripts/VARSCANscript.py " + bnlist[i] + " " + r[i] + " " + outdir + "\""
	print "sbatch --partition=LONG /mnt/DATA/home4/arc/hb493/bin/submit_sbatch5.sh"
	print "export SBATCH_CMD=\"\""
	
for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python /mnt/DATA/home4/arc/hb493/scripts/GATKcallingscript.py " + bnlist[i] + " " + r[i] + " " + outdir2 + "\""
	print "sbatch --partition=LONG /mnt/DATA/home4/arc/hb493/bin/submit_sbatch6.sh"
	print "export SBATCH_CMD=\"\""




