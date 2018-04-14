#!/usr/local/bin/python

import os
import sys
import os.path

import numpy

# Take arguments
if len(sys.argv)<>5:
	print("Error: wrong number of arguments")


outdir = sys.argv[1]
print(outdir)
ExAC_file = sys.argv[2]
print(ExAC_file)
gene_file = sys.argv[3]
print(gene_file)
ped_file=sys.argv[4]
print(ped_file)
# # Check Autism Genes
f = open(gene_file, "r")
genelist = f.readlines()
f.close()

output_dir = outdir + "/GeneOutput/"

cmnd = "mkdir " + output_dir
print(cmnd)
os.system(cmnd)

#load ExAC data  and extract useful info- Save it to a hash
f = open(ExAC_file,"r")
lines = f.readlines()
f.close()
snp_data = {}
for line in lines:
	line = line.replace("\n","")
	if (line.find("#") ==0):
		pass
	else:
		snp_array = line.split("\t")
		# key is chr:pos:refG
		key_start = snp_array[0] + ":" + snp_array[1] + ":" + snp_array[3] + ":"
		#may have more than one alternate alleles
		all_snps = snp_array[4].split(",")
		data = snp_array[5]
		for i in range(6,len(snp_array)):
			data = data + "\t" + snp_array[i]
	
		#extract allele freq from ExAC
		EXAC_data = data.split("\t")
		exac_split = EXAC_data[2].split(";")
		ac_adjs_str = exac_split[3][7:]
		ac_adjs = ac_adjs_str.split(",")
		an_adjs_str = exac_split[19][7:]
		an_adjs = int(an_adjs_str)
		
		for i in range(len(all_snps)):
			key = all_snps[i]
			ac_adj = int(ac_adjs[i])
			an_adj = int(an_adjs)
			if (an_adj > 1):
				freq = float(ac_adj) / float(an_adj)
			else:
				freq = 0
			data = str(ac_adj) + "\t" + str(an_adj) + "\t" + str(freq)
			snp_data[key_start + key] = data


for g in genelist:
	gene = g.replace("\n","")
	gf=open(output_dir + "/%s.ExAC.xls"  %gene, 'w+')
	gstr = "|" + gene + "|"
	print(gstr)
	if (len(gene)>0):
		for fname in os.listdir(outdir):
			if fname.endswith('.txt') and fname.startswith("LP"):
				if os.path.isfile(fname):
					bname =  fname.split(".")[0]
					ft = open(fname)
					lines = ft.readlines()
					ft.close()
					for line in lines:
						line = line.replace("\n", "")
						if gstr in line:
							if not "intron_variant" in line and not "prime"  in line  and not "intergenic_region" in line and not "upstream_gene_variant" in line and not "synonymous_variant" in line:
								#print(bname)
								print(line)
								data=line.split("\t")
								# "egrep \"" + gene + "\\|\" *.txt | grep -v intron | grep -v prime | grep -v intergenic | grep -v upstream | egrep -v \"synonymous_variant\""
								key = data[0]  + ":" + data[1] + ":" + data[3] + ":" + data[4]
								#print(key)
								
								line_out = ""
								if (snp_data.has_key(key)):
									EXAC = snp_data[key]
									line_out = line_out + "\t1\t" + str(EXAC)
									#print line
									new_line= bname
									for i in range (0,len(data)):
										new_line =  new_line + "\t" + data[i]
									new_line = new_line + "\t" + str(EXAC) + "\t-\t-"
									gf.write(new_line + "\n")
									
								else:
									if (key.find("Chrom") == 0):
										new_line = bname
										for i in range (0,len(data)):
											new_line = new_line + "\t" + data[i]
										new_line = new_line + "\t\tIn ExAC\tAC_ADJ\tAN_ADJ\tFreq\tLink (hg19)" # \tExAC Orig 1\tExAC Orig 2\tExAC Orig 3"
										gf.write(new_line + "\n")
									else:
										new_line= bname
										for i in range (0,len(data)):
											new_line =  new_line + "\t" + data[i]
										new_line = new_line + "\t0" + "\t-\t-\t-\t-" #\t\t\t"
										gf.write(new_line + "\n")
		gf.close()
		



cmnd = "Rscript Checkped.R " + output_dir + " " + ped_file
print(cmnd)
os.system(cmnd)
