#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir =os.path.dirname("path/indir") # QC output dir
outdir = os.path.dirname("path/outdir")


bnlist=[]
endlist=[]

# identify r_1.fq.gz files
for file in os.listdir(indir):
	# save the basename  and ending	
	fbasename = file.split(".QC.r_1", 1)[0]
	if (fbasename!=file):
		ending = file.split(".QC.r_1", 1)[1]
		# identify corresponding r_2 file
		f2 = fbasename + ".QC.r_2" + ending
		f9 = fbasename + ".QC.r_9" + ending

		
		if os.path.isfile(indir +"/"+f2):
			if not (fbasename in bnlist):
				
				if os.path.isfile(indir +"/"+ f9):
					if not (fbasename in bnlist):
						bnlist.append(fbasename)
						endlist.append(ending)
				else:
					print ("no r_9 file found for " + fbasename + ".QC.r_1" + ending)
		else:
			print ("no r_2 file found for " + fbasename + ".QC.r_1" + ending)

# generate lists:
r1=[]
r2=[]
r9=[]
for i in range(len(bnlist)):
	r1.append(indir + "/" + bnlist[i] + ".QC.r_1" + endlist[i])
	r2.append(indir + "/" + bnlist[i] + ".QC.r_2" + endlist[i])
	r9.append(indir + "/" + bnlist[i] + ".QC.r_9" + endlist[i])

for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python BOWTIEscript.py " + bnlist[i] + " " + r1[i] + " " + r2[i] + " " + outdir +  " " + r9[i] + "\""
	print "sbatch --partition=1604 submit_sbatch2.sh"
	print "export SBATCH_CMD=\"\""

#	print ("python BOWTIEscript.py " + bnlist[i] + " " + r1[i] + " " + r2[i])




