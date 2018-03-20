
#!/usr/local/bin/python

import os
import sys
import os.path


# Take arguments

if len(sys.argv)<>4:
	print("Error: wrong number of arguments")

indir = sys.argv[1]
outdir = sys.argv[2]
ExAC_file = "/mnt/b2/home4/arc/hb493/ExAC.r0.3.1.sites.vep.vcf"
gene_file = "/mnt/b2/home4/arc/hb493/Autism_Genes_Sparks"
ped_file= sys.argv[3]

for f in os.listdir(indir):
    if f.endswith('.vcf'):
        print ("snpEff")
        print f
        cmnd = "java -Xmx32g -jar /mnt/b2/home4/arc/hb493/bin/snpeff/snpEff/snpEff.jar GRCh37.75 " +  indir + "/" + f + " > " + outdir + "/" + f + ".SnpEff.txt"
        print(cmnd)
        os.system(cmnd)




cmnd =  "python /mnt/b2/home4/arc/hb493/scripts/pipB37/Annotation.py " + outdir  + " " + ExAC_file + " " + gene_file + " " + ped_file
print(cmnd)
os.system(cmnd)


#cmnd = "Rscript /mnt/b2/home4/arc/hb493/scripts/pipB37/Checkped.R"


# # # Run SNPEff
# cmnd = "for f in " + indir + "*.vcf do echo \"snpEff $f\" done"
# #cmnd = "for f in " + indir + "/*.vcf do echo \"snpEff $f\" \\n java -Xmx32g -jar ./snpeff/snpEff/snpEff.jar hg38 $f > " + outdir + "/$f.SnpEff.txt done;"
# os.system(cmnd)
# print cmnd