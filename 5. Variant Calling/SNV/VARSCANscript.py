#!/usr/local/bin/python

import os
import sys
import os.path


# Take arguments

if len(sys.argv)<>4:
	print("Error: wrong number of arguments")

basename = sys.argv[1]
f1 = sys.argv[2]
outdir = sys.argv[3]

# SNPS

# mpileup

ref = "/mnt/DATA/home4/arc/hb493/hg38/hg38.fa"
out = outdir + "/" + basename + ".mpileup"
cmnd = "samtools_mt mpileup -B -d 100000 -f " + ref + " " + f1 + " > " + out
print(cmnd)
os.system(cmnd)


# SNP calling

out2 = outdir + "/" + basename + ".VARSCAN.vcf"
cmnd = "varscan  mpileup2snp " + out + " > " + out2 + " --min-var-freq 0.01 --output-vcf"
print(cmnd)
os.system(cmnd)

#index vcf file
out3 = outdir + "/" + basename + ".VARSCAN.vcf.gz"
cmnd = "bgzip -c " + out2 + " > " + out3
print(cmnd)
os.system(cmnd)

cmnd = "tabix -p vcf " + out3
print(cmnd)
os.system(cmnd)
 







	




