#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders

#indir =os.path.dirname("/mnt/DATA/home4/arc/hb493/NA12878/BWAMEM/")
#outdir = os.path.dirname("/mnt/DATA/home4/arc/hb493/NA12878/BWAMEM/")


indir1 = os.path.dirname("/mnt/DATA/home4/arc/hb493/GF7/output/VC/VARSCAN/")
indir2 = os.path.dirname("/mnt/DATA/home4/arc/hb493/GF7/output/VC/GATK/")
outdir = os.path.dirname("/mnt/DATA/home4/arc/hb493/GF7/output/VC/ALL/")

#indir =os.path.dirname("/mnt/DATA/home4/arc/hb493/Rimma_fastq/PICARD/output/")
#outdir = os.path.dirname("/mnt/DATA/home4/arc/hb493/Rimma_fastq/GATK/output/")
# identify VARSCAN files

l1=[]
l2=[]
bnlist=[]


for file in os.listdir(indir1):
	
	fbasename = file.split(".VARSCAN.vcf.gz", 1)[0]
	if (fbasename!=file):
		if(file == fbasename + ".VARSCAN.vcf.gz"):
		# identify corresponding GATK file
			f2 = fbasename + ".GATK.vcf.gz"
			if os.path.isfile(indir2 +"/"+f2):
				if not (fbasename in bnlist):
					bnlist.append(fbasename)
					l1.append(indir1+ "/" + file)
					l2.append(indir2 + "/" + f2)
			else:
				print ("no GATK file found for " + fbasename + ".VARSCAN.vcf.gz")





for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"/mnt/DATA/home4/arc/hb493/bin/vcftools/src/perl/vcf-merge " + l1[i] + " " + l2[i] + " | bgzip -c > " + outdir + "/" + bnlist[i] + ".ALL.vcf.gz" + "\""
	print "sbatch --partition=LONG /mnt/DATA/home4/arc/hb493/bin/submit_sbatch7.sh -n 4" 
	print "export SBATCH_CMD=\"\""




