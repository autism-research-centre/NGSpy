#!/usr/local/bin/python

import os
import os.path
import re

#define input and output folders
indir = "path/indir" #CONVERT output dir
outdir = "path/outdir"


bnlist=[]
endlist=[]
nfiles =[]
# identify r_1.fq.gz files
for file in os.listdir(indir):
	# save the basename  and ending	
	fbasename = file.split(".r_1", 1)[0]
	if (fbasename!=file):
		ending = file.split(".r_1", 1)[1]
		# identify corresponding r_2 file
		f2 = fbasename + ".r_2" + ending
		f9 = fbasename + ".r_9" + ending
		if os.path.isfile(indir +"/"+f2):
			if not (fbasename in bnlist):
				if os.path.isfile(indir +"/"+ f9):
					if not (fbasename in bnlist):
						bnlist.append(fbasename)
						endlist.append(ending)
						nfiles.append(3)
				else:
					#print ("no r_9 file found for " + fbasename + ".r_1" + ending)
					bnlist.append(fbasename)
					endlist.append(ending)
					nfiles.append(2)
					
		else:
			print ("no r_2 file found for " + fbasename + ".r_1" + ending)

			
#print(bnlist)
#print(endlist)



r1=[]
r2=[]
r9=[]

for i in range(len(bnlist)):
	r1.append(indir + "/" + bnlist[i] + ".r_1" + endlist[i])
	r2.append(indir + "/" + bnlist[i] + ".r_2" + endlist[i])
	if nfiles[i]==3:
		r9.append(indir + "/" + bnlist[i] + ".r_9" + endlist[i])
	else:
		r9.append("")


for i in range(len(bnlist)):
	print "export SBATCH_CMD=\"\""
	print "export SBATCH_CMD=\"python QCscript.py " + bnlist[i] + " " + r1[i] + " " + r2[i] + " 4 " + outdir + " " + r9[i] + "\""
	print "sbatch --partition=LONG submit_sbatch1.sh -n 4" 
	print "export SBATCH_CMD=\"\""

#	print ("python QCscript.py " + bnlist[i] + " " + r1[i] + " " + r2[i])




