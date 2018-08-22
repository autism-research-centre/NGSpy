#load libraries
library("IRanges")
library("GenomicRanges")

#function that merges two dataframes containing CNVs. minfrac denotes the overlap percentage required. 1 is full overlap. 
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

#minfrac=1 : restrictive merging. Taking only CNVs that are fullly overlapped between ERDS and CNVnator
minfrac <-1
#identify CNVNator files
cnt_files <- list.files(path="cnvnator_GATK", pattern="*.calls.cnvnator")

for (cf in cnt_files)
  {
  #identify the basename (ID)
  bn <- unlist(strsplit(cf, split=".calls.cnvnator"))
  # Identify corresponding ERDS file (same basename)
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
