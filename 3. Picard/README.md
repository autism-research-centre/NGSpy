# PICARD

After the alignment of the reads to the reference genome, two of the steps common to all the pipelines are marking the read groups and marking the duplicates. 
These are useful and necessary steps for downstream analyses. Both steps are usually done with a toolkit called PICARD.

One necessary step after the read alignment to the reference genome is to mark the read groups.
The read group information is mandatory for downstream GATK analyses (GATK will not work without a read group tag). 

The MarkDuplicates tool from PICARD identifies read pairs with the same orientation that have the exact same 5′ start position in the mapping. 
Then, the read pair with the highest mapping quality score is retained and the other read pairs are flagged as duplicates. 

As every step of the pipeline, it is designed to be submitted to the cluster for sets of files (for exmaple families) simultaneously.
Slurm is used for submitting the jobs to the cluster. 

This folder contains:
  1. The main script:  	PICARDscript.py (and BOWTIEscript.py)
  2. The submission script:  	submitPICARDscript.py (and submitBOWTIEscript.py)

## Dependencies:
This step makes use of the following software(s): 
   * PICARD tools (https://broadinstitute.github.io/picard/)

