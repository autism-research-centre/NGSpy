# Variant Calling



This step consists on the processing of post-alignment reads into high-quality variant calls. 

Many tools are available to perform the variant calling step. 
Comparative studies have indicated that the variant callers available in the Genome Analysis ToolKit (GATK) show the best performance. 
However, there are reports showing other variant callers that can outperform GATK, questioning the notion that GATK should be considered a gold-standard for variant calling[5]. 
For most applications, a comprehensive strategy combining GATK variant calls with those made by another method (such as Samtools or Varscan) is likely to provide the most comprehensive result. 
Combining multiple calling approaches improves both sensitivity and specificity of the final set of variants.

Here both GATK HaplotypeCaller and Varscan are applied. GATKHC remains the preferred option. 
As every step of the pipeline, it is designed to be submitted to the cluster for sets of files (for example families) simultaneously.
Slurm is used for submitting the jobs to the cluster. 

This folder contains:
  1. The main script:  	GATKHCscript.py (and VARSCANscript.py)
  2. The submission script:  	submitGATKHCscript.py (and submitVARSCANscript.py)
  

## Dependencies:
This step makes use of the following software(s):
   * GATK (https://software.broadinstitute.org/gatk/)

