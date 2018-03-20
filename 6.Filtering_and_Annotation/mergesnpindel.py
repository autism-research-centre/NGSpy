#!/usr/local/bin/python

import os
import sys
import os.path

# Take arguments

if len(sys.argv)<>5:
	print("Error: wrong number of arguments")


basename=sys.argv[1]
f1=sys.argv[2]
f2=sys.argv[3]
outdir=sys.argv[4]


indelNH = outdir + "/" + basename + ".indel.NH.vcf"  
cmnd = "egrep -v \"^#\"" + f2 + " > " + indelNH
os.system(cmnd)
print(cmnd)
snpbis = outdir + "/" + basename + ".snp.bis.vcf"
cmnd = "cp " + f1 + " " + snpbis
os.system(cmnd)
print(cmnd)
cmnd = "cat " + indelNH + " >> " + snpbis
os.system(cmnd)
print(cmnd)
out = outdir + "/" + basename + ".snp.indel.vcf"
cmnd = "perl /mnt/DATA/home4/arc/hb493/hg38/vcfsorter.pl /mnt/DATA/home4/arc/hb493/hg38/hg38.dict " + snpbis + " > " + out
os.system(cmnd)
print(cmnd)

cmnd = "rm " +  indelHH g+ " " + snpbis
os.system(cmnd)
print(cmnd)


