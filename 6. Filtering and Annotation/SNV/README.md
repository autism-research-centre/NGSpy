# FILTERING and ANNOTATION  

This step consists on performing a primary filtering step to the original variants obtained from the previous steps of the pipeline.
Additionaly, scripts for spliting the variants into variants belonging to a common set (UK biobank) and non-common in the sense they are not reported in the set of common variants.
Finally, a primary annotation of the variants as well as a selection of variants with a Mendelian pattern of inheritance within the families are performed.

This folder contains:
  1. The FILTER scripts: 
        * FILTERscript.py 
        * submitFILTERscript.py
  2. The COMMON scripts that seleects common variants
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
   
   
  
  
