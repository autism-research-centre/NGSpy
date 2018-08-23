# FILTERING and ANNOTATION  

This section contains the primary filtering step for the original variants obtained from the previous steps of the pipeline.
Additionaly, it includes the description of how to split the variants into variants belonging to a common set (UK biobank) and non-common in the sense they are not reported in the set of common variants.
Finally, a primary annotation of the variants as well as a selection of variants with a Mendelian pattern of inheritance within the families is also included.

This folder contains:
  1. The FILTER scripts: 
        * FILTERscript.py 
        * submitFILTERscript.py
  2. The COMMON scripts that splits the variants dataset into a set of common variants and a set of non-common variants. 
        * COMMONscript.py 
        * submitCOMMONscript.py
  3. The Annotation scripts:
        * ANnotation.py
        * ANNOTATONscript.py 
        * submitANNOTATONscript.py
      
## Dependencies

 This step makes use of the following software(s):
   * GATK (https://software.broadinstitute.org/gatk/) for the filtering
   * vcftools (vcf-isec) for intersecting variants with a common set of variants
   * snpEff (http://snpeff.sourceforge.net/) for Annotating the variants
   
   
  
  
