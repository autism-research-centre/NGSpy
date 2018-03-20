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


#SV calling


# BREAKDANCER
out = outdir + "/" + basename + ".breakdancer.cfg"
cmnd = "/mnt/DATA/home4/arc/hb493/bin/bam2cfg.pl " + f1 + " > " +  out
print(cmnd)
os.system(cmnd)

out2 = outdir + "/" + basename + ".breakdancer.sv"
cmnd = "/mnt/DATA/home4/arc/hb493/bin/breakdancer-max " + out + " > " + out2
print(cmnd)
os.system(cmnd)

#PINDEL

cfg = outdir + "/" + basename + ".pindelcfg.txt"
f= open(cfg, "w")
f.write( f1 + " 500 " + basename + "\n")
f.close()

out6 = outdir + "/" + basename + ".pindel" 
cmnd = "/mnt/home3/hb493/pindel -f " + ref + " -i " + cfg + " -c ALL -o " + out6 
print(cmnd)
os.system(cmnd)

#o1 = outdir + "/" + basename + ".pindel_D"
#if not (os.stat(o1).st_size == 0):
#	o1vcf = outdir + "/" + basename + ".pindel_D.vcf"
#	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o1 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o1vcf
#	print(cmnd)
#	os.system(cmnd)

#o2 = outdir + "/" + basename + ".pindel_SI"
#if not (os.stat(o2).st_size == 0):
#	o2vcf = outdir + "/" + basename + ".pindel_SI.vcf"
#	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o2 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o2vcf
#	print(cmnd)
#	os.system(cmnd)


#o3 = outdir + "/" + basename + ".pindel_LI"
#if not (os.stat(o3).st_size == 0):
#	o3vcf = outdir + "/" + basename + ".pindel_LI.vcf"
#	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o3 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o3vcf
#	print(cmnd)
#	os.system(cmnd)
	
#o4 = outdir + "/" + basename + ".pindel_INV"
#if not (os.stat(o4).st_size == 0):
#	o4vcf = outdir + "/" + basename + ".pindel_INV.vcf"
#	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o4 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o4vcf
#	print(cmnd)
#	os.system(cmnd)	
	
# o5 = outdir + "/" + basename + ".pindel_TD"
# if not (os.stat(o5).st_size == 0):
# 	o5vcf = outdir + "/" + basename + ".pindel_TD.vcf"
# 	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o5 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o5vcf
# 	print(cmnd)
# 	os.system(cmnd)
# 
# o6 = outdir + "/" + basename + ".pindel_BP"
# if not (os.stat(o6).st_size == 0):
# 	o6vcf = outdir + "/" + basename + ".pindel_BP.vcf"
# 	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o6 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o6vcf
# 	print(cmnd)
# 	os.system(cmnd)
# 
# o7 = outdir + "/" + basename + ".pindel_CloseEndMapped"
# if not (os.stat(o7).st_size == 0):
# 	o7vcf = outdir + "/" + basename + ".pindel_CloseEndMapped.vcf"
# 	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o7 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o7vcf
# 	print(cmnd)
# 	os.system(cmnd)
# 	
# o8 = outdir + "/" + basename + ".pindel_INT_final"
# if not (os.stat(o8).st_size == 0):
# 	o8vcf = outdir + "/" + basename + ".pindel_INT_final.vcf"
# 	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o8 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o8vcf
# 	print(cmnd)
# 	os.system(cmnd)
# 	
# o9 = outdir + "/" + basename + ".pindel_RP"
# if not (os.stat(o9).st_size == 0):
# 	o9vcf = outdir + "/" + basename + ".pindel_RP.vcf"
# 	cmnd = "/mnt/DATA/home4/arc/hb493/bin/pindel2vcf -p " + o9 + " -r " + ref + "  -R GRCh38.primary.Assembly -d 20131217 -v " + o9vcf
# 	print(cmnd)
# 	os.system(cmnd)	
# 	
	
	
#DELLY
outdelly = outdir + "/" + basename + ".bcf"
cmnd = "/mnt/DATA/home4/arc/hb493/bin/delly/src/delly call -t DEL -g " + ref + " -x " +  dellyexcl + " -o " + outdelly  + " " + f1
print(cmnd)
os.system(cmnd)

	
	
#BreaKmer
#cfg = outdir + "/" + basename + ".breaKmer.cfg"
#f= open (cfg, "w")
#fwrite("analysis_name="+ basename + "\n")
#fwrite("targets_bed_file=/mnt/DATA/home4/arc/hb493/bin/breaKmer/pedfiles/chr1.bed\n")
#fwrite("sample_bam_file=" + f1 + + "\n")
#fwrite("analysis_dir="+ outdir + "\n")
#fwrite("reference_data_dir=/mnt/DATA/home4/arc/hb493/hg38\n")
#fwrite("cutadapt_config_file=/mnt/DATA/home4/arc/hb493/bin/breaKmer/cutadapt.conf\n")
#fwrite("cutadapt=/usr/bin/cutadapt\n") 
#fwrite("jellyfish=/usr/bin/jellyfish\n")
#fwrite("blat=/usr/bin/blat\n")
#fwrite("blat_port=??\n")
#fwrite("gfclient=/usr/bin/gfClient\n")
#fwrite("gfserver=/usr/bin/gfServer\n")
#fwrite("fatotwobit=/usr/bin/faToTwoBit\n")
#fwrite("reference_fasta=" + ref + "\n")
#fwrite("gene_annotation_file=/mnt/DATA/home4/arc/hb493/bin/breaKmer/gencode.v20.chr_patch_hapl_scaff.annotation.gtf\n")
#fwrite("kmer_size=15\n")
##other_regions_file=<path to bed file containing targeted unannotated cluster regions, OPTIONAL> 
##repeat_mask_file=<path to ucsc_hg19_rmsk.bed, OPTIONAL>
##alternate_fastas=<comma delimited list of the paths to alternate fasta files, such as HuRef or CHM1, OPTIONAL>
##normal_bam_file=<path to normal bam file, OPTIONAL>
#fclose




	




