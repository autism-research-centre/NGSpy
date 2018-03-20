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


ref = "/mnt/DATA/home4/arc/hb493/hg38/hg38.fa"

#RDXplorer

cmnd = "python rdxplorer.py " + f1 + " " + ref + " " + outdir + " All M HG38 100 2 10 True True True"
print(cmnd)
os.system(cmnd)

#FREEC

# CREATE CONFIG FILE


# RUN FREEC
 cmnd="/mnt/home3/hb493/bin2/FREEC-10.6/src/freec -conf " + SLX-9999.freec.cfg 
