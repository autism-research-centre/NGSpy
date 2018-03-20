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
    

Each of these steps has a dedicated python script meant to be submitted in a high performance computing cluster through SLURM


# REQUIREMENTS


## Software Requirements

The pipeline has several software dpendencies:

Stage | Dependencies    | Internal dependencies
------------ | -------------| ---------------
ALL | samtools (currently running with Version: 0.1.19)|  -     
0-CONVERT | bam2fastx |     -       
1-QC      | sickle |       -       
   "     | trim-galore | cutadapt
2-Mapping | bwa-mem (version 0.6 or higher)|     -       
3-PICARD | PICARD tools |     -     
4-GATK | Genome Analysis ToolKit (version 3.7-0)|    -    
5-VC | Genome Analysis ToolKit (version 3.7-0)|    -
  "  | VARSCAN (version 2.3)|   -
6-Filtering and Annotation | Genome Analysis ToolKit (version 3.7-0)|    -
" |SNPEff (version 4.3) | - 
7- CNV | CNVnator | root
" |erds (version 1.1)|
8-SV | Breakdancer | - 
" | Pindel | -
" | Delly | - 


## Data Requirements

Many of the step use external data:


Stage | Data file    | Example: current file name 
------------ | -------------| -------------
2-Mapping | Reference Genome| Ensembl_GRCh37.ordered.fa
4-GATK | Reference Genome| Ensembl_GRCh37.ordered.fa
"      | Known SNPs | 1000G_phase1.snps.high_confidence.b37.sorted.vcf.gz
"      | Known Indels | Mills_and_1000G_gold_standard.indels.b37.sorted.vcf.gz
5-VC | Reference Genome| Ensembl_GRCh37.ordered.fa
"      | Known SNPs | 1000G_phase1.snps.high_confidence.b37.sorted.vcf.gz
"      | Known Indels | Mills_and_1000G_gold_standard.indels.b37.sorted.vcf.gz
6-Filtering and Annotation | Reference Genome| Ensembl_GRCh37.ordered.fa
"      | ExAC | ExAC.r0.3.1.sites.vep.vcf
7- CNV | Reference Genome| Ensembl_GRCh37.ordered.fa
8- SV | Reference Genome| Ensembl_GRCh37.ordered.fa

