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


ref = "ref.fa"


#PINDEL

# STEP 1: Creates and generates the appropriate info into a config file
cfg = outdir + "/" + basename + ".pindelcfg.txt"
f= open(cfg, "w")
f.write( f1 + " 500 " + basename + "\n")
f.close()

# STEP 2 :. Run PINDEL
out6 = outdir + "/" + basename + ".pindel" 
cmnd = "pindel -f " + ref + " -i " + cfg + " -c ALL -o " + out6 
print(cmnd)
os.system(cmnd)



	
