#!/usr/local/bin/python

import os
import sys
import os.path

# Take arguments
r9 = False
if len(sys.argv)<6:
	print("Error: wrong number of arguments")
if len(sys.argv)>7:
	print("Error: wrong number of arguments")

basename=sys.argv[1]
f1=sys.argv[2]
f2=sys.argv[3]
n=sys.argv[4]
outdir=sys.argv[5]

if (len(sys.argv) >=7):
	r9 = True
	f9 = sys.argv[6]

# Run sickle

out1 = outdir + "/" + basename + ".r_1_trimmed.fastq"
out2 = outdir + "/" + basename + ".r_2_trimmed.fastq"
outs = outdir + "/" + basename + ".single_trimmed.fastq"

cmnd ="sickle pe -f " + f1 + " -r " + f2 + " -t sanger -o " + out1 + " -p " + out2 + " -s " + outs + " -q 20 - l 20"
print(cmnd)
os.system(cmnd)


# IF R9 is TRUE
if (r9 == True):
	outs2 = outdir + "/" + basename + ".SE_trimmed.fastq"
	cmnd ="sickle se -f " + f9 + " -t sanger -o " + outs2 + " -q 20 - l 20"
	print(cmnd)
	os.system(cmnd)
	cmnd2 = " cat " + outs2 + " >> " + outs


# Run trim_galore
in1 = outdir + "/" + basename + ".r_1_trimmed.fastq"
in2 = outdir + "/" + basename + ".r_2_trimmed.fastq"
ints = outdir + "/" + basename + ".single_trimmed.fastq"

cmnd = "trim_galore -o " + outdir + " --paired --illumina --gzip " + in1 + " " + in2
print(cmnd)
os.system (cmnd)

	
cmnd =  "trim_galore -o " + outdir + " --illumina --gzip " + ints
print(cmnd)
os.system (cmnd)


#Rename output files names

o1 =  outdir + "/" + basename + ".r_1_trimmed_val_1.fq.gz"
o2 =  outdir + "/" + basename + ".r_2_trimmed_val_2.fq.gz" 
o3 = outdir + "/" + basename + ".single_trimmed_trimmed.fq.gz" 
no1 = outdir + "/" + basename + ".QC.r_1.fq.gz"
no2 = outdir + "/" + basename +  ".QC.r_2.fq.gz"
no3 = outdir + "/" + basename + ".QC.r_9.fq.gz" 
c1 ="mv " + o1 + " " + no1
c2 = "mv " + o2 + " " + no2
c3 = "mv " + o3 + " " + no3

print(c1)
print(c2)
print(c3)
os.system(c1)
os.system(c2)
os.system(c3)


#Exit cleanly
if (os.path.isfile(no1)):
	cc1 = "rm " + in1 + " " + in1 + "_trimming_report.txt"
	os.system(cc1)
if (os.path.isfile(no2)):
	cc2 = "rm " + in2 + " " + in2 + "_trimming_report.txt" + " " + outs2
	os.system(cc2)
if (os.path.isfile(no3)):
	cc3 = "rm " + ints + " " + ints + "_trimming_report.txt" 	
	os.system(cc3)




