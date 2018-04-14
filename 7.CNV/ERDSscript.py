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


ref = "Ensembl_GRCh37.ordered.fa"

vcfdir = outdir + "/../../VC/GATK"
vcfinput = vcfdir + "/" + basename + ".GATK.vcf"


# ERDS
newdir = outdir + "/" + basename

cmnd = "mkdir " + newdir
print(cmnd)
os.system(cmnd)



cmnd= "perl erds_pipeline.pl -b " + f1 + " -v " + vcfinput + " -o " + newdir + " -r "+ ref
print(cmnd)
os.system(cmnd)







