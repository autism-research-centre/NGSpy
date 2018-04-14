#usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("path/indir") #output from FILTER script
outdir = os.path.dirname("path/outdir")
ped_file= "ped.fam"


print "export SBATCH_CMD=\"\""
print "export SBATCH_CMD=\"python ANNOTATIONscript.py " + indir + " " + outdir +  " " + ped_file + "\""
print "sbatch --partition=ERDS /mnt/DATA/home4/arc/hb493/bin/submit_sbatch15.sh"
print "export SBATCH_CMD=\"\""

#	print ("python CONVERTscript.py " + bnlist[i] + " " + r[i] + " " + outdir)
