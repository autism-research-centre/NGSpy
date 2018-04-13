# GATK

The GATK Best Practices pipeline runs a set of programs which (1) realign and (2) recalibrate the quality of previously mapped reads. 
These steps are recommended by the Broad Institute to get the best calls out of a set of mapped reads using their variant calling methods. 

Base Quality Score Recalibration is a data pre-processing step that detects systematic errors made by the sequencer when it estimates the quality score of each base call. 
Base quality score recalibration (BQSR) is a process in which we apply machine learning to model these errors empirically and adjust the quality scores accordingly.
The base recalibration process involves two key steps: first the program builds a model of covariation based on the data and a set of known variants, then it adjusts the base quality scores in the data based on the model. The known variants are used to mask out bases at sites of real (expected) variation, to avoid counting real variants as errors.


The local realignment process is designed to locally realign reads such that the number of mismatching bases is minimized across all the reads. In general, regions requiring local realignment are due to the presence of an insertion or deletion (indels) in the individual's genome with respect to the reference genome. 
The indel realignment is a two-steps process: (1) it identifies regions where alignments may potentially be improved (RealignerTargetCreator tool) and (2) it realigns the reads in these regions using a consensus model that takes all reads in the alignment context together (IndelRealigner tool).


As every step of the pipeline, it is designed to be submitted to the cluster for sets of files (for exmaple families) simultaneously.
Slurm is used for submitting the jobs to the cluster. 

This folder contains:
  1. The main script:  	GATKscript.py 
  2. The submission script:  	submitGATKscript.py

## Dependencies:
This step makes use of the following software(s): 
   * GATK (https://software.broadinstitute.org/gatk/)
