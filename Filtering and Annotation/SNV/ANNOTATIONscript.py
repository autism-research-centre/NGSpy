
#!/usr/local/bin/python

import os
import sys
import os.path


# Take arguments

if len(sys.argv)<>4:
	print("Error: wrong number of arguments")

indir = sys.argv[1]
outdir = sys.argv[2]
ExAC_file = "ExAC.r0.3.1.sites.vep.vcf"
gene_file = "Autism_Genes_Sparks"
ped_file= sys.argv[3]

#Annotation with snpEff
for f in os.listdir(indir):
    if f.endswith('.vcf'):
        print ("snpEff")
        print f
        cmnd = "java -Xmx32g -jar snpEff.jar GRCh37.75 " +  indir + "/" + f + " > " + outdir + "/" + f + ".SnpEff.txt"
        print(cmnd)
        os.system(cmnd)


#Annotation of variants in autism Genes with ExAC and inheritance within the family.
cmnd =  "python Annotation.py " + outdir  + " " + ExAC_file + " " + gene_file + " " + ped_file
print(cmnd)
os.system(cmnd)


