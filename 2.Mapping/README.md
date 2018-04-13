# MAPPING

The mapping step is one of the most important steps in any NGS data analysis. 
Mapping refers to the process of aligning short reads to the complete reference genome sequence. 

Two methods have been tested in order to select the optimal mapping tool for these samples. Those are BWA-MEM and BOWTIE2.

BWA-MEM was finally chosen as the aligner for this pipeline but BOWTIE2-related scripts are keeped for their eventual use in the future.
As every step of the pipeline, it is designed to be submitted to the cluster for sets of files (for exmaple families) simultaneously.
Slurm is used for submitting the jobs to the cluster. 

This folder contains:
  1. The main script:  	BWAMEMscript.py (and BOWTIEscript.py)
  2. The submission script:  	submitBWAMEMscript.py (and submitBOWTIEscript.py)

## Dependencies:
This step makes use of the following software(s):
   * BWA-MEM (http://bio-bwa.sourceforge.net/)
   * BOWTIE2 (http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)
   * Samtools for indexing, sorting and merging 

