# QC



This step consists on performing a Quality Control (QC) procedure over the fastq files obtained in the previous step 


As every step of the pipeline, it is designed to be submitted to the cluster for sets of files (for exmaple families) simultaneously.
Slurm is used for submitting the jobs to the cluster. 

This folder contains:
  1. The main script:  	QCscript.py
  2. The submission script:  	submitQCscript.py

## Dependencies:
This step makes use of the following software(s):
   * Trim-galore (https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/) for quality and adapter trimming 
   * Sickle (https://github.com/najoshi/sickle) for adaptive quality trimming

