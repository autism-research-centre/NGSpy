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


ref = "/mnt/DATA/home4/arc/hb493/hg38/hg38.fa"
dellyexcl = "/mnt/DATA/home4/arc/hb493/hg38/hg38.delly.excl"



	
#DELLY
#deletions
out = outdir + "/" + basename + ".del.bcf"
cmnd = "delly call -t DEL -g " + ref + " -x " +  dellyexcl + " -o " + out  + " " + f1
print(cmnd)
os.system(cmnd)

#bcftools is found in the same src directory as delly after its installation
outdelly = outdir + "/" + basename + ".delly_del.vcf"
cmnd = "bcftools view " + out + " > " +  outdelly
print(cmnd)
os.system(cmnd)

#insertions
out2 = outdir + "/" + basename + ".ins.bcf"
cmnd = "delly call -t INS -g " + ref + " -x " +  dellyexcl + " -o " + out2  + " " + f1
print(cmnd)
os.system(cmnd)

outdelly2 = outdir + "/" + basename + "delly_ins.vcf"
cmnd = "bcftools view " + out2 + " > " +  outdelly2
print(cmnd)
os.system(cmnd)

#inversions	
out3 = outdir + "/" + basename + ".inv.bcf"
cmnd = "delly call -t INV -g " + ref + " -x " +  dellyexcl + " -o " + out3  + " " + f1
print(cmnd)
os.system(cmnd)

outdelly3 = outdir + "/" + basename + "delly_inv.vcf"
cmnd = "bcftools view " + out3 + " > " +  outdelly3
print(cmnd)
os.system(cmnd)


#duplications	
out4 = outdir + "/" + basename + ".dup.bcf"
cmnd = "delly call -t DUP -g " + ref + " -x " +  dellyexcl + " -o " + out4  + " " + f1
print(cmnd)
os.system(cmnd)

outdelly4 = outdir + "/" + basename + "delly_dup.vcf"
cmnd = "bcftools view " + out4 + " > " +  outdelly4
print(cmnd)
os.system(cmnd)



#Translocations
out5 = outdir + "/" + basename + ".tra.bcf"
cmnd = "delly call -t TRA -g " + ref + " -x " +  dellyexcl + " -o " + out5  + " " + f1
print(cmnd)
os.system(cmnd)

outdelly5 = outdir + "/" + basename + "delly.tra.vcf"
cmnd = "bcftools view " + out5 + " > " +  outdelly5
print(cmnd)
os.system(cmnd)



