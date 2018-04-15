
library("IRanges")
library("GenomicRanges")

mergeOverlapping <- function(x, y, minfrac=1) {
  dx <-dim(x)
  dy <- dim(y)
  p1<- which(names(y)=="chr")
  p2<-which(names(y)=="start")
  p3<-which(names(y)=="end")
  p4 <- which(names(y)=="length")
  x2 <- with(x, GRanges(chr, IRanges(as.numeric(start), as.numeric(end))))
  y2 <- with(y, GRanges(chr, IRanges(as.numeric(start), as.numeric(end))))
  hits <- findOverlaps(x2, y2)
  h <- as.data.frame(hits)
  xov <- x[h$queryHits,]
  yov <- y[h$subjectHits,]
  xhits <- x2[queryHits(hits)]
  yhits <- y2[subjectHits(hits)]
  frac <- width(pintersect(xhits, yhits)) / pmin(width(xhits), width(yhits))
  merge <- frac >= minfrac
  
  xovf <- xov[merge,]
  yovf <- yov[merge,]
  merged <- cbind(xovf, yovf)
  names(merged)[c(dx[2]+p1, dx[2]+p2, dx[2]+p3, dx[2]+p4)] <- c("chr_2", "start_2", "end_2", "length_2")
  merged
}

minfrac <-1

cnt_files <- list.files(path="cnvnator_PICARD", pattern="*.calls.cnvnator")

for (cf in cnt_files)
  {
  bn <- unlist(strsplit(cf, split=".calls.cnvnator"))
  if(file.exists(paste("erds_PICARD/", bn, "/20.events", sep="")))
    {
    #READ CNVNATOR DATA
    cnt <- read.table(paste("cnvnator_PICARD/", cf, sep=""))
    p <- do.call(rbind, strsplit(as.character(cnt$V2), ':'))
    cnt$chr <- p[,1]
    p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
    cnt$start <- p2[,1]
    cnt$end <-p2[,2]
    cnt <- cnt[,-2]
    names(cnt)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
    
    #FILTERING
    cntf <- subset(cnt, pval1<0.05 & q0<0.5)
    
    #READ ERDS DATA
    erds<- read.table(paste("erds_PICARD/", bn, "/20.events", sep=""))
    names(erds) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
    #FILTERING
    erdsf <- subset(erds, !is.na(summed_score))
    
    
    # MERGE ERDS and CNVNATOR
    m<- mergeOverlapping(cntf, erdsf, minfrac = minfrac)
    write.table(m, file=paste(bn, ".cnvs.txt", sep=""), col.names=T, row.names=F, quote=F)
    }
  else
    {
    cat(paste("ERROR: erds file not found for:", bn))
    }
  }
  


# 
# #-----------------------------LP2100030-DNA_A01-----------------------------
# 
# #READ CNVNATOR DATA
# cnt1 <- read.table("cnvnator_GATK/LP2100030-DNA_A01.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt1$V2), ':'))
# cnt1$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt1$start <- p2[,1]
# cnt1$end <-p2[,2]
# cnt1 <- cnt1[,-2]
# names(cnt1)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt1f <- subset(cnt1, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds1<- read.table("erds_GATK/LP2100030-DNA_A01/20.events")
# names(erds1) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds1f <- subset(erds1, !is.na(summed_score))
# 
# 
# # MERGE ERDS and CNVNATOR
# m1<- mergeOverlapping(cnt1f, erds1f, minfrac = minfrac)
# 
# 
# #-----------------------------LP2100030-DNA_A02-----------------------------
# 
# #READ CNVNATOR DATA
# cnt2 <- read.table("cnvnator_GATK/LP2100030-DNA_A02.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt2$V2), ':'))
# cnt2$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt2$start <- p2[,1]
# cnt2$end <-p2[,2]
# cnt2 <- cnt2[,-2]
# names(cnt2)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# #FILTERING
# cnt2f <- subset(cnt2, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds2<- read.table("erds_GATK/LP2100030-DNA_A02/20.events")
# names(erds2) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds2f <- subset(erds2, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m2<- mergeOverlapping(cnt2f, erds2f, minfrac = minfrac)
# 
# 
# #-----------------------------LP2100030-DNA_A03-----------------------------
# #READ CNVNATOR DATA
# cnt3 <- read.table("cnvnator_GATK/LP2100030-DNA_A03.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt3$V2), ':'))
# cnt3$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt3$start <- p2[,1]
# cnt3$end <-p2[,2]
# cnt3 <- cnt3[,-2]
# names(cnt3)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt3f <- subset(cnt3, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds3<- read.table("erds_GATK/LP2100030-DNA_A03/20.events")
# names(erds3) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds3f <- subset(erds3, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m3<- mergeOverlapping(cnt3f, erds3f, minfrac = minfrac)
# 
# 
# #-----------------------------LP2100030-DNA_A04-----------------------------
# #READ CNVNATOR DATA
# cnt4 <- read.table("cnvnator_GATK/LP2100030-DNA_A04.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt4$V2), ':'))
# cnt4$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt4$start <- p2[,1]
# cnt4$end <-p2[,2]
# cnt4 <- cnt4[,-2]
# names(cnt4)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt4f <- subset(cnt4, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds4<- read.table("erds_GATK/LP2100030-DNA_A04/20.events")
# names(erds4) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds4f <- subset(erds4, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m4<- mergeOverlapping(cnt4f, erds4f, minfrac = minfrac)
# 
# 
# #-----------------------------LP2100030-DNA_A05-----------------------------
# #READ CNVNATOR DATA
# cnt5 <- read.table("cnvnator_GATK/LP2100030-DNA_A05.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt5$V2), ':'))
# cnt5$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt5$start <- p2[,1]
# cnt5$end <-p2[,2]
# cnt5 <- cnt5[,-2]
# names(cnt5)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt5f <- subset(cnt5, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds5<- read.table("erds_GATK/LP2100030-DNA_A05/20.events")
# names(erds5) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds5f <- subset(erds5, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m5<- mergeOverlapping(cnt5f, erds5f, minfrac = minfrac)
# 
# 
# #-----------------------------LP2100030-DNA_A06-----------------------------
# #READ CNVNATOR DATA
# cnt6 <- read.table("cnvnator_GATK/LP2100030-DNA_A06.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt6$V2), ':'))
# cnt6$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt6$start <- p2[,1]
# cnt6$end <-p2[,2]
# cnt6 <- cnt6[,-2]
# names(cnt6)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt6f <- subset(cnt6, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds6<- read.table("erds_GATK/LP2100030-DNA_A06/20.events")
# names(erds6) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds6f <- subset(erds6, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m6<- mergeOverlapping(cnt6f, erds6f, minfrac = minfrac)
# 
# 
# #-----------------------------LP2100030-DNA_A07-----------------------------
# #READ CNVNATOR DATA
# cnt7 <- read.table("cnvnator_GATK/LP2100030-DNA_A07.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt7$V2), ':'))
# cnt7$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt7$start <- p2[,1]
# cnt7$end <-p2[,2]
# cnt7 <- cnt7[,-2]
# names(cnt7)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt7f <- subset(cnt7, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds7<- read.table("erds_GATK/LP2100030-DNA_A07/20.events")
# names(erds7) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds7f <- subset(erds7, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m7<- mergeOverlapping(cnt7f, erds7f, minfrac = minfrac)
# 
# 
# #-----------------------------LP2100030-DNA_A08-----------------------------
# #READ CNVNATOR DATA
# cnt8 <- read.table("cnvnator_GATK/LP2100030-DNA_A08.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt8$V2), ':'))
# cnt8$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt8$start <- p2[,1]
# cnt8$end <-p2[,2]
# cnt8 <- cnt8[,-2]
# names(cnt8)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt8f <- subset(cnt8, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds8<- read.table("erds_GATK/LP2100030-DNA_A08/20.events")
# names(erds8) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds8f <- subset(erds8, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m8<- mergeOverlapping(cnt8f, erds8f, minfrac = minfrac)
# 
# 
# #-----------------------------LP2100030-DNA_A09-----------------------------
# #READ CNVNATOR DATA
# cnt9 <- read.table("cnvnator_GATK/LP2100030-DNA_A09.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt9$V2), ':'))
# cnt9$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt9$start <- p2[,1]
# cnt9$end <-p2[,2]
# cnt9 <- cnt9[,-2]
# names(cnt9)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt9f <- subset(cnt9, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds9<- read.table("erds_GATK/LP2100030-DNA_A09/20.events")
# names(erds9) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds9f <- subset(erds9, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m9<- mergeOverlapping(cnt9f, erds9f, minfrac = minfrac)
# 
# 
# 
# #-----------------------------LP2100082-DNA_B01-----------------------------
# #READ CNVNATOR DATA
# cnt10 <- read.table("cnvnator_GATK/LP2100082-DNA_B07.calls.cnvnator")
# p <- do.call(rbind, strsplit(as.character(cnt10$V2), ':'))
# cnt10$chr <- p[,1]
# p2 <- do.call(rbind, strsplit(as.character(p[,2]), '-'))
# cnt10$start <- p2[,1]
# cnt10$end <-p2[,2]
# cnt10 <- cnt10[,-2]
# names(cnt10)[1:8] <- c("type", "length", "RDnorm", "pval1", "pval2", "pval3", "pval4", "q0")
# 
# #FILTERING
# cnt10f <- subset(cnt10, pval1<0.05 & q0<0.5)
# 
# #READ ERDS DATA
# erds10<- read.table("erds_GATK/LP2100082-DNA_B07/20.events")
# names(erds10) <- c("chr", "start", "end", "length", "type", "summed_score","precise_boundary", "reference_cn", "inferred_cn")
# #FILTERING
# erds10f <- subset(erds10, !is.na(summed_score))
# 
# # MERGE ERDS and CNVNATOR
# m10<- mergeOverlapping(cnt10f, erds10f, minfrac = minfrac)
# 
