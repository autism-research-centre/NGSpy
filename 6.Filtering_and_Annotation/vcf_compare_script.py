#!/usr/local/bin/python

import os
import sys
import os.path

import numpy

# Take arguments

if len(sys.argv)<>4:
	print("Error: wrong number of arguments")
basename = sys.argv[1]
f1=sys.argv[2]
outdir = sys.argv[3]


ref_common = "/mnt/b2/home4/arc/hb493/UKB/hrcukbfreqpruned.v2.vcf.gz"

outcom = outdir + "/" + basename + ".common.vcf"
outnocom = outdir + "/" + basename + ".no_common.vcf" 

#BGZIP + TABIX

out2 = outdir + "/" + basename+ ".vcf.gz"
cmnd = "bgzip -c " + f1 + " > " + out2
print(cmnd)
os.system(cmnd)
cmnd = "tabix -p vcf " + out2
print(cmnd)
os.system(cmnd)


# COMMON
cmnd = "/mnt/b2/home4/arc/hb493/bin/vcftools/src/perl/vcf-isec -n +2 " + out2 + " " + ref_common + " > " + outcom
print(cmnd)
os.system(cmnd)

# NON_COMMON
cmnd = "/mnt/b2/home4/arc/hb493/bin/vcftools/src/perl/vcf-isec -c " + out2 + " " + ref_common + " > " + outnocom
print(cmnd)
os.system(cmnd)


#EXIT CLEANLY
cmnd= "rm " + out2
print(cmnd)
os.system(cmnd)

out3= outdir + "/" + basename+ ".vcf.gz.tbi"
cmnd= "rm " + out2
print(cmnd)
os.system(cmnd)
