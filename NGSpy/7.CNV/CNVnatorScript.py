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


# CNVnator

#STEP 1 : 

outroot = outdir + "/" + basename + ".root"
outcnv = outdir + "/" + basename + ".calls.cnvnator"

# cmnd = "cnvnator -root " + outroot + " -genome GRCh37 -chrom ALL -tree " + f1
# STEP 1 EXTRACT READ MAPPING
cmnd = "cnvnator -root " + outroot + " -genome " + ref + " -chrom 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y -tree " + f1 +  " -d /mnt/DATA/home4/arc/hb493/b37/chrfa -unique"
print(cmnd)
os.system(cmnd)

#STEP 2 GENERATING A HISTOGRAM

cmnd = "cnvnator -root " + outroot + " -genome " + ref + " -chrom 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y -his 100 -d /mnt/DATA/home4/arc/hb493/b37/chrfa"
print(cmnd)
os.system(cmnd)

# STEP3 CALCULATING STATS

cmnd = "cnvnator -root " + outroot + " -genome " + ref + " -chrom 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y -stat 100 -d /mnt/DATA/home4/arc/hb493/b37/chrfa"
print(cmnd)
os.system(cmnd)

# STEP 4 RD SIGNAL PARTITIONING

cmnd = "cnvnator -root " + outroot + " -genome " + ref + " -chrom 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y -partition 100 -d /mnt/DATA/home4/arc/hb493/b37/chrfa"
print(cmnd)
os.system(cmnd)

# STEP 5 CNV CALLING

cmnd = "cnvnator -root " + outroot + " -genome " + ref + " -chrom 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y -call 100 -d /mnt/DATA/home4/arc/hb493/b37/chrfa > " + outcnv  
print(cmnd)
os.system(cmnd)








