#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir = "/mnt/DATA/home4/arc/hb493/fam1/output/VCALLING/raw/"
outdir = "/mnt/DATA/home4/arc/hb493/fam1/output/VCALLING/raw/"

#input_dir = os.path.dirname(/mnt/DATA/home4/arc/hb493/Rimma_fastq)
#output_dir = os.path.dirname(/mnt/DATA/home4/arc/hb493/Rimma_fastq)
bnlist=[]
endlist=[]
nfiles =[]
# identify r_1.fq.gz files
for file in os.listdir(indir):
	# save the basename  and ending	
	fbasename = file.split(".snp.vcf", 1)[0]
	if (fbasename!=file):
		# identify corresponding indel file
		f2 = fbasename + ".indel.vcf"
		if os.path.isfile(indir +"/"+f2):
			if not (fbasename in bnlist):
				bnlist.append(fbasename)	
		else:
			print ("no indel file found for " + fbasename + ".snp.vcf")

			
#print(bnlist)
#print(endlist)



r1=[]
r2=[]


for i in range(len(bnlist)):
	r1.append(indir + "/" + bnlist[i] + ".snp.vcf")
	r2.append(indir + "/" + bnlist[i] + ".indel.vcf")
	

for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python /mnt/DATA/home4/arc/hb493/scripts/mergesnpindel.py " + bnlist[i] + " " + r1[i] + " " + r2[i] + " " + outdir + "\""
	print "sbatch --partition=1604 /mnt/DATA/home4/arc/hb493/bin/submit_sbatch.sh -n 4" 
	print "export SBATCH_CMD=\"\""

#	print ("python QCscript.py " + bnlist[i] + " " + r1[i] + " " + r2[i])




