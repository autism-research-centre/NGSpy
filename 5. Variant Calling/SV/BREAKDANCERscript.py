
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



# BREAKDANCER

#STEP 1 : Generates a config file for breakdancer to work properly
out = outdir + "/" + basename + ".breakdancer.cfg"
cmnd = "path/bam2cfg.pl " + f1 + " > " +  out
print(cmnd)
os.system(cmnd)


# STEP 2: run Breakdancer
out2 = outdir + "/" + basename + ".breakdancer.sv"
cmnd = "/path/breakdancer-max " + out + " > " + out2
print(cmnd)
os.system(cmnd)
