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


# SORT bam files

out = outdir + "/" + basename + ".sorted.bam"
cmnd = "samtools_mt sort -n -@ 8 " + f1 +  " -o " + out + " -m 5000000000"
print(cmnd)
os.system(cmnd)

# CREATE ADDITIONAL BAM FILES FOR SUPPLEMENTARY ALIGNMENTS

out2 = outdir + "/" + basename + ".SE.sam"
out3 = outdir + "/" + basename + ".SE.bam"
cmnd = "samtools view -H " + out + "  > " + out2
print(cmnd)
os.system(cmnd)


cmnd = "samtools_mt view -@ 8 -h " + out + " | awk \'{ if(and($2,0x800)) {printf \"%s\\t\", $1; t=$2-2048; printf \"%s\\t\" , t; for (i=3; i<NF; i++){printf \"%s\\t\", $i} ; printf \"%s\\n\",$NF;}}\' >> " + out2
print(cmnd)
os.system(cmnd)


cmnd = "samtools_mt view -Sb " + out2 + " > " + out3
print(cmnd)
os.system(cmnd)

# CONVERT to FASTQ : 
out4 = outdir + "/" + basename + ".fastq"
out5 = outdir + "/" + basename + ".SE.fastq" 
cmnd1= "bam2fastx -PANQ -o " + out4 + " " + out
print(cmnd1)
os.system(cmnd1)
cmnd2 = "bam2fastx -ANQ -o " + out5 + " " + out3 
print(cmnd2)
os.system(cmnd2)

o41 = outdir + "/" + basename + ".1.fastq"
o42 = outdir + "/" + basename + ".2.fastq"

no41 = outdir + "/" + basename + ".r_1.fastq"
no42 = outdir + "/" + basename + ".r_2.fastq"

no5 = outdir + "/" + basename + ".r_9.fastq"


cmnd = "mv " + o41 + " " + no41
print(cmnd)
os.system(cmnd)
cmnd = "mv " + o42 + " " + no42
print(cmnd)
os.system(cmnd)
cmnd = "mv " + out5 + " " + no5
print(cmnd)
os.system(cmnd)

o61 = outdir + "/" + basename + ".r_1.fastq.gz"
o62 = outdir + "/" + basename + ".r_2.fastq.gz"
o69 = outdir + "/" + basename + ".r_9.fastq.gz"

cmnd = "sed 's/K/J/g' " + no41 + " | gzip -9 > " + o61
print(cmnd)
os.system(cmnd)

cmnd = "sed 's/K/J/g' " + no42 + " | gzip -9 > " + o62
print(cmnd)
os.system(cmnd)

cmnd = "sed 's/K/J/g' " + no5 + " | gzip -9 > " + o69
print(cmnd)
os.system(cmnd)


#Exit cleanly

cmnd = "rm " + out + " " + out2 + " " + out3 + " " + no41 + " " + no42 + " " + no5
print(cmnd)
os.system(cmnd)

