#!/usr/local/bin/python

import os
import sys
import os.path


# Take arguments

if len(sys.argv)<>6:
	print("Error: wrong number of arguments")
r9 = False
basename = sys.argv[1]
f1 = sys.argv[2]
f2 = sys.argv[3]
outdir = sys.argv[4]

if (len(sys.argv) >=6):
	r9 = True
	f9 = sys.argv[5]



# Run bwa-mem

out = outdir + "/" + basename + ".QC.MAP.sam"
cmnd = "bwa mem -M -t 24 Ensembl_GRCh37.fa " + f1 + " " + f2 +" > " + out
print(cmnd)
os.system(cmnd)

# SAM to BAM
outb = outdir + "/" + basename + ".QC.MAP.bam"
cmnd = "samtools_mt  view -@ 8 -b -1 " + out + " > " + outb
print(cmnd)
os.system(cmnd)

#SORT
outsort   = outdir + "/" + basename + ".QC.MAP.s.bam"
cmnd = "samtools_mt sort -@ 8 -m 5000000000 " + outb + " -o " + outsort
print(cmnd)
os.system(cmnd)

outm = outdir + "/" + basename + ".QC.MAP.s.m.bam"

# IF R9 is TRUE (if there is a SE file)
if (r9 == True):
	#BWA-MEM
	out9 = outdir + "/" + basename + ".9.QC.MAP.sam"
	cmnd = "bwa mem -M -t 16 Ensembl_GRCh37.fa " + f9 + " > " + out9
	print(cmnd)
	os.system(cmnd)
	#SAM to BAM
	outb9 = outdir + "/" + basename + ".9.QC.MAP.bam"
	cmnd = "samtools_mt  view -@ 8 -b -1 " + out9 + " > " + outb9
	print(cmnd)
	os.system(cmnd)
	#SORT
	outsort9   = outdir + "/" + basename + ".9.QC.MAP.s.bam"
	cmnd = "samtools_mt sort -@ 8 " + outb9 + " -o " + outsort9
	print(cmnd)
	os.system(cmnd)
	#MERGE
	cmnd = "samtools_mt merge -f " + outm + " " + outsort + " " + outsort9
	print(cmnd)
	os.system(cmnd)
else:
	cmnd = "mv " + outsort + " " + outm
	print(cmnd)
	os.system(cmnd)
	


#INDEX
cmnd = "samtools_mt  index " + outm
print(cmnd)
os.system(cmnd)


	
#Exit cleanly

if (os.path.isfile(outm)):
	c1 = "rm " + out + " " + outb + " " + outsort + " " + out9 + " " + outb9 + " " + outsort9
	print(c1)
	os.system(c1)



