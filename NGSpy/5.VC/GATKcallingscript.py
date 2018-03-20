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

#GATK

cmnd = "samtools_mt  index " + f1
print(cmnd)
os.system(cmnd)

ref = "/mnt/DATA/home4/arc/hb493/b37/Ensembl_GRCh37.ordered.fa"
out = outdir + "/" + basename + ".GATK.vcf"
cmnd = "java -jar /mnt/DATA/home4/arc/hb493/bin/GenomeAnalysisTK.jar -R " + ref + " -T HaplotypeCaller -I " + f1 + " -o " + out
print(cmnd)
os.system(cmnd)

cmnd = "sed -i '/^#/ s/20$/LP2100082-DNA_B03/g' " + out
print(cmnd)
os.system(cmnd)


out2 =  outdir + "/" + basename + ".GATK.vcf.gz"

cmnd = "bgzip -c " + out + " > " + out2
print(cmnd)
os.system(cmnd)
cmnd = "tabix -p vcf " + out2
print(cmnd)
os.system(cmnd)



	


