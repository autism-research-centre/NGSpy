# CONVERT



This step consists on converting the bam files obtained from the sequencing platform (provided by Illumina) into fastq files


Every step of te pipeline is designed to be submitted to the cluster for sets of files (for exmaple families) simultaneously.
Slurm is used for submitting the jobs to the cluster. 

This folder contains:
  1. The main script:  	CONVERTscript.py
  2. The submission script:  	submitCONVERTscript.py

