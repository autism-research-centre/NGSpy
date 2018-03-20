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

ref = "/mnt/DATA/home4/arc/hb493/b37/Ensembl_GRCh37.ordered.fa"


#split multiallelic variants


outsplit = outdir + "/" + basename + ".split.vcf"
cmnd = "/mnt/b2/home4/arc/hb493/bin/bcftools/bcftools norm -m -any " + f1 + " > " + outsplit
print(cmnd)
os.system(cmnd)


# select SNPS
outs = outdir + "/" + basename + ".snps.vcf.gz"

cmnd = "vcftools --vcf " + outsplit + " --remove-indels --recode --stdout | bgzip -c > " + outs
print(cmnd)
os.system(cmnd)

cmnd = "gunzip " + outs
print(cmnd)
os.system(cmnd)


# select INDELS
outi = outdir + "/" + basename + ".indels.vcf.gz"
cmnd = "vcftools --vcf " + outsplit + " --keep-only-indels --recode --stdout | bgzip -c > " + outi
print(cmnd)
os.system(cmnd)


cmnd = "gunzip " + outi
print(cmnd)
os.system(cmnd)

outs = outdir + "/" + basename + ".snps.vcf"
outi = outdir + "/" + basename + ".indels.vcf"
# QD  and MD fiter
outfilt_snps = outdir + "/" + basename + ".snps.f1.vcf"
cmnd = "java -jar /mnt/DATA/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T VariantFiltration -R " + ref + " -V " + outs + " --filterExpression \"QD < 2.0 || MQ < 40.0\" --filterName \"snp_QD_MQ\" -o " + outfilt_snps 
print(cmnd)
os.system(cmnd)

outfilt_indels = outdir + "/" + basename + ".indels.f1.vcf"
cmnd = "java -jar /mnt/DATA/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T VariantFiltration -R " + ref + " -V " + outi + " --filterExpression \"QD < 2.0 || MQ < 40.0\" --filterName \"indel_QD_MQ\" -o " + outfilt_indels 
print(cmnd)
os.system(cmnd)


outfs = outdir + "/" + basename + ".snps.filtered.vcf"
cmnd = "java -jar /mnt/DATA/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T SelectVariants -R " + ref + " -V " + outfilt_snps + " -select 'vc.isNotFiltered()' -o " + outfs
print(cmnd)
os.system(cmnd)


outfi = outdir + "/" + basename + ".indels.filtered.vcf"
cmnd = "java -jar /mnt/DATA/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T SelectVariants -R " + ref + " -V " + outfilt_indels + " -select 'vc.isNotFiltered()' -o " + outfi
print(cmnd)
os.system(cmnd)

#SOR filter
outfilt2_snps = outdir + "/" + basename + ".snps.f2.vcf"
cmnd = "java -jar /mnt/DATA/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T VariantFiltration -R " + ref + " -V " + outfs + " --filterExpression \"SOR > 3.0\" --filterName \"snp_SOR\" -o " + outfilt2_snps 
print(cmnd)
os.system(cmnd)


outfilt2_indels = outdir + "/" + basename + ".indels.f2.vcf"
cmnd = "java -jar /mnt/DATA/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T VariantFiltration -R " + ref + " -V " + outfi +  " --filterExpression \"SOR > 10.0\" --filterName \"indel_SOR\" -o " + outfilt_indels 
print(cmnd)
os.system(cmnd)

#EXIT CLEANLY

cmnd = "rm "+ outsplit + " " + outfilt_indels + " " + outfilt_snps
print(cmnd)
os.system(cmnd)



	




