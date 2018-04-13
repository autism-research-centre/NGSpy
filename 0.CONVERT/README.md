# CONVERT



This step consists on converting the bam files obtained from the sequencing platform (provided by Illumina) into fastq files


Every step of the pipeline is designed to be submitted to the cluster for sets of files (for exmaple families) simultaneously.
Slurm is used for submitting the jobs to the cluster. 

This folder contains:
  1. The main script:  	CONVERTscript.py
  2. The submission script:  	submitCONVERTscript.py

## Dependencies
This step makes use of the following software(s):
   * Samtools (https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/) for converting bam to sam and sam to bam
   * bam2fastx (https://github.com/najoshi/sickle) for converting bam to fastq
  
  

