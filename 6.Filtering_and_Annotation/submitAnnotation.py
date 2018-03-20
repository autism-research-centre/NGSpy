#usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("/mnt/b2/home4/arc/hb493/GF12/output/b37/VC/FILTER/")
outdir = os.path.dirname("/mnt/b2/home4/arc/hb493/GF12/output/b37/VC/Annotate/")
ped_file= "/mnt/b2/home4/arc/hb493/GFamilies/pedigrees/GF12.fam"


print "export SBATCH_CMD=\"\""
print "export SBATCH_CMD=\"python /mnt/DATA/home4/arc/hb493/scripts/pipB37/AnnotationPIP.py " + indir + " " + outdir +  " " + ped_file + "\""
print "sbatch --partition=ERDS /mnt/DATA/home4/arc/hb493/bin/submit_sbatch15.sh"
print "export SBATCH_CMD=\"\""

#	print ("python CONVERTscript.py " + bnlist[i] + " " + r[i] + " " + outdir)