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


ref = "/mnt/DATA/home4/arc/hb493/b37/Ensembl_GRCh37.ordered.fa"

vcfdir = outdir + "/../../VC/GATK"
vcfinput = vcfdir + "/" + basename + ".GATK.vcf"


# ERDS
newdir = outdir + "/" + basename

cmnd = "mkdir " + newdir
print(cmnd)
os.system(cmnd)



cmnd= "perl /mnt/home3/hb493/bin2/erds1.1/erds_pipeline.pl -b " + f1 + " -v " + vcfinput + " -o " + newdir + " -r "+ ref
print(cmnd)
os.system(cmnd)







