#load libraries
library(stringi)
#Take arguments

args <- commandArgs(TRUE)
if (length(args)!=2){
	stop(" two argument should be supplied (input dir with gene outputs and ped file).n", call.=FALSE)
}else{
	indir <- as.character(args[1])
	ped_file <-as.character(args[2])
}

#Identify gene files
gene_files <- list.files(path = indir, pattern = "*.ExAC.xls")

#define col names for result table  Aff_r is the rate of affected individuals with the variants (within the family) and NonAff_r is the rate of non-affected individuals with the variants (within the family)
#For BAP MAP NAP rates are for variants exclusive to each category
#For diagnosis
var_table <- c("Vchr", "Vpos", "snp_Eff", "Aff_r", "NonAff_r")
#For BAP/MAP/NAP
var_table <- c("Vchr", "Vpos", "snp_Eff", "var_BAP_r", "var_MAP_r", "var_NAP_r")

#for each gene, read the file and for every unique variant, match with the pedigree and count variants present in affected and non-affected subjects

for (i in c(1:length(gene_files)))
  {
  gene_table <- try(read.table(paste(indir, "/", gene_files[i], sep="")), silent=T)
  
  if(class(gene_table)=="data.frame")
    {
    print(gene_files[i])
    names(gene_table)[1:9] <- c("ID", "chr", "pos", "VID", "Ref", "Alt", "QUAL", "FILTER", "snpEff")
    ped <- read.table(ped_file)
    gene_table$ID <- as.factor(gene_table$ID)
    ped$ID <- as.factor(ped$V2)
    gene_table_with_ped <- merge(gene_table, ped, by="ID")
    unique_variants <- unique(gene_table_with_ped$pos)
    for (k in (1:length(unique_variants)))
      {
      variant_table <- gene_table_with_ped[which(gene_table_with_ped$pos==unique_variants[k]),]
      var_chr <- unique(variant_table$chr)
      var_pos <- unique(variant_table$pos)
      var_snpEff <- as.character(variant_table$snpEff[1])
      # For diagnosis
      #var_Aff_r <- sum(variant_table$V6==2)/sum(ped$V6==2)
      #var_nonAff_r <- sum(variant_table$V6==1)/sum(ped$V6==1)
      #var_table<- rbind(var_table, c(var_chr, var_pos, var_snpEff, var_Aff_r, var_nonAff_r))
      
      #For BAP/MAP/NAP
      var_BAP_r <- sum(variant_table$V6=="BAP")/sum(ped$V6=="BAP")
      var_MAP_r <- sum(variant_table$V6=="MAP")/sum(ped$V6=="MAP")
      var_NAP_r <- sum(variant_table$V6=="NAP")/sum(ped$V6=="NAP")
      var_table<- rbind(var_table, c(var_chr, var_pos, var_snpEff, var_BAP_r, var_MAP_r, var_NAP_r))
      }
    }
}
#formatting output table
if (!is.null(dim(var_table)))
{
  vt <- as.data.frame(var_table)
  vt <- vt[-1,]
  # For diagnosis
  # names(vt) <- c("Vchr", "Vpos", "snpEff", "Aff_r", "NonAff_r")
  ##For BAP/MAP/NAP
  names(vt) <- c("Vchr", "Vpos", "snpEff", "BAP", "MAP", "NAP")
  write.table(vt, file=paste(indir, "/AV_all.txt", sep=""), row.names=F,col.names=T, quote=F)

# For diagnosis
#df1 <- subset(vt, Aff_r==1)
#df2 <- subset(df1, NonAff_r==0)

#For BAP/MAP/NAP
df1 <- subset(vt, BAP==1 & MAP==0 & NAP==0)
df2 <- subset(vt, MAP==1 & BAP==0 & NAP==0)
df3 <- subset(vt, NAP==1& MAP==0 & BAP==0)
  
# For diagnosis	
#  if(dim(df1)[1]>0)
#    write.table(df1, file=paste(indir, "/AV_aff.txt", sep=""), row.names=F, col.names=T, quote=F)
#  if(dim(df2)[1]>0)
#    write.table(df2, file=paste(indir, "/AV_allAff.txt", sep=""), row.names=F, col.names=T, quote=F)
  
#For BAP/MAP/NAP
if(dim(df1)[1]>0)
    write.table(df1, file=paste(indir, "/AV_BAP.txt", sep=""), row.names=F, col.names=T, quote=F)
  if(dim(df2)[1]>0)
    write.table(df2, file=paste(indir, "/AV_MAP.txt", sep=""), row.names=F, col.names=T, quote=F)
  if(dim(df3)[1]>0)
    write.table(df3, file=paste(indir, "/AV_NAP.txt", sep=""), row.names=F, col.names=T, quote=F)	
}


