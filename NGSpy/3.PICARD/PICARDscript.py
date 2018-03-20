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



# Mark Duplicates

out = outdir + "/" + basename + ".QC.MAP.s.MDup.bam"
met= outdir + "/" + basename + ".metrics.txt"
cmnd = "picard-tools MarkDuplicates I=" + f1 + " O=" + out + " M=" + met
print(cmnd)
os.system(cmnd)

# Add read groups

out2 = outdir + "/" + basename + ".QC.MAP.s.MDup.RGr.bam"
cmnd = "picard-tools AddOrReplaceReadGroups I=" + out + " O=" + out2 + " CREATE_INDEX=TRUE RGID=1 RGLB=lib1 RGPL=illumina RGPU=unit1 RGSM=20" 
#picard-tools AddReplaceReadGroups I=/mnt/DATA/home4/arc/hb493/Rimma_fastq/PICARD/output_1M/SLX-9999.QC.mapped-sorted.MarkDuplicates.bam O=/mnt/DATA/home4/arc/hb493/Rimma_fastq/PICARD/output_1M/SLX-9999.QC.mapped-sorted.MarkDuplicatesReadGroups.bam RGID=1 RGLB=lib1 RGPL=illumina RGPU=unit1 RGSM=20
print(cmnd)
os.system(cmnd)


	
#Exit cleanly

if (os.path.isfile(out2)):
	#c1 ="rm " + out
	c1 ="rm " + out + " " + met
	print(c1)
	os.system(c1)



