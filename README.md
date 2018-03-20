# NGSpy


Next-Generation Sequencing Data Analysis Pipeline with Python scripts


This repository is aimed to provide the basic scripts of a pipeline of Whole Genome Sequencing Data Analysis

# PIPELINE Structure

The pipeline has the following structure:

    0. CONVERT
        - Converting bam files (provided by the sequencing platform/company) into paired-end fastq files
    1. QC
        - Performing the QC on fastqc files
    2. Mapping
        - Mapping the reads to a given reference genome
    3. PICARD
        - Marking the duplicates and adding read groups information
    4. GATK
        - Base Recalibration and Indel Realignment
    5.VC
        - Variant calling
    6. Filtering and Annotation
        - provides tools to filter and annotate genetic variants called by the GATK *HaplotypeCaller*
    7. CNV
        - Performs the CNV calling
     8. SV
        - Performs Structural Variant calling
    

# REQUIREMENTS


## Software Requirements



## Data Requirements
