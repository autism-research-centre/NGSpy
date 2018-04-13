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


# Index bam file
# cmnd = "samtools_git index " + f1
# print(cmnd)
# os.system(cmnd)

ref = "GRCh37.fa"
knownSNPs = "1000G_phase1.snps.high_confidence.b37.sorted.vcf.gz"
knownIndels = "Mills_and_1000G_gold_standard.indels.b37.sorted.vcf.gz"

#### BASE RECALIBRATION
#out1 = outdir + "/" + basename + ".QC.MAP.s.MDup.RGr.rMQ.bam"
outab = outdir + "/" + basename + ".QC.MAP.s.MDup.RGr.BRec-table.grp"
out = outdir + "/" + basename + ".QC.MAP.s.MDup.RGr.BRec.bam"

#reassign mapped reads quality 255 -> 60 (only BOWTIE)
# cmnd = "java -jar /mnt/DATA/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T PrintReads -R " + ref + " -I " + f1 + " -o " + out1 + " -rf ReassignOneMappingQuality -RMQF 255 -RMQT 60 " 
# print(cmnd)
# os.system(cmnd)

# generate a base recalibration table 
cmnd = "java -jar /mnt/beegfs/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T BaseRecalibrator -R " + ref + " -I " + f1 + " -o " + outab + " --knownSites " + knownSNPs + " -nct 8 --disable_auto_index_creation_and_locking_when_reading_rods -U ALLOW_SEQ_DICT_INCOMPATIBILITY"
print(cmnd)
os.system(cmnd)

#Recalibrate bam file
cmnd = "java -jar /mnt/beegfs/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T PrintReads -R " + ref + " -I " + f1 + " -BQSR " + outab + " -o " + out + " -nct 8"
print(cmnd)
os.system(cmnd)


##### INDEL REALIGNMENT
out2 = outdir + "/" + basename + ".QC.MAP.s.MDup.RGr.BRec.IReal.bam"
outint = outdir + "/" + basename + ".intervals"
#create intervals
cmnd =  "java -jar /mnt/beegfs/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T RealignerTargetCreator -R " + ref + " -I " + out + " -known " + knownIndels + " -o " + outint + " -U ALLOW_SEQ_DICT_INCOMPATIBILITY"
print(cmnd)
os.system(cmnd)

# realign
cmnd = "java -jar /mnt/beegfs/home4/arc/hb493/bin/GenomeAnalysisTK.jar -T IndelRealigner -R " + ref + " -I " + out + " -known " + knownIndels + " -o " + out2 + " -targetIntervals " + outint + " -U ALLOW_SEQ_DICT_INCOMPATIBILITY"
print(cmnd)
os.system(cmnd)


	
#Exit cleanly

if (os.path.isfile(out2)):
	c1 ="rm " + outab + " " + outint + " " + out
	print(c1)
	os.system(c1)



