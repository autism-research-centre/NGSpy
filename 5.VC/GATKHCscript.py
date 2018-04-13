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
#index bam file
cmnd = "samtools_mt  index " + f1
print(cmnd)
os.system(cmnd)

#variant calling
ref = "Ensembl_GRCh37.ordered.fa"
out = outdir + "/" + basename + ".GATK.vcf"
cmnd = "java -jar GenomeAnalysisTK.jar -R " + ref + " -T HaplotypeCaller -I " + f1 + " -o " + out
print(cmnd)
os.system(cmnd)

#change sample name in vcf file
cmnd = "sed -i '/^#/ s/20/" + basename + "/g' " + out
print(cmnd)
os.system(cmnd)

#index vcf file
out2 =  outdir + "/" + basename + ".GATK.vcf.gz"
cmnd = "bgzip -c " + out + " > " + out2
print(cmnd)
os.system(cmnd)
cmnd = "tabix -p vcf " + out2
print(cmnd)
os.system(cmnd)



	


