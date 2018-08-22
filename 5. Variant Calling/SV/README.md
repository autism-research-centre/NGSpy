# Structural Variant Calling



This step consists on the processing of post-alignment reads into structural variant calls. 

Many tools are available to perform the structural variant calling step. 
The four most commonly used techniques for calling SV are:
*	**CL: Clustering**
    * Clustering methods aim to group reads supporting the same SV together
    * BREAKDANCER - LUMPY - DELLY
*	**SA: Split-read alignments**
    * Split-reads alignment tries to align soft-clipped reads and one-end-anchored reads to either find the matching breakpoints (indirect case) or refine the breakpoints identified by discordantly mapped reads (direct case).
    * PINDEL - LUMPY - DELLY
*	**As: Assembly-based**
    * Contig Assembly: Paired reads may be too short to accurately locate the SVs. Some SV callers proposed that we can assemble paired reads into contigs. When the contigs are long enough, it is easier to locate the breakpoints of the SVs. Different SV callers may use different methods to build the contigs.
    * Whole Genome Assembly:  longer contigs assembled from short reads. Can be more accurately aligned to the genome
    * Local  assembly: used to assemble only reads with an initial alignment to some locus in the reference genome. Used to detect SV in exons or to validate SV found by SA methods
    * SVABA
*	**ST: Statistical testing**
    * Statistical models are used for CNV detection to verify the observed read-depth against to null distributions (i.e., distribution without the CNVs). 
    * Statistical methods are also used by general SV calling methods to derive a confidence score for filtering and ranking the predictions. For example, BREAKDANCER computes confidence score based on the reads mappings, measuring the depth and breadth of the clusters.
    * BREAKDANCER - DELLY

Among the existing methods, we have chosen 3 different SV callers according to then following criteria:
(i)	Ability to detect as many different types of SV as possible
(ii)	Popularity and reference in the scientific community
(iii)	Availability and easiness of installation compilation and use. 

The selected softwares for SV detection were:
  1.  Breakdancer
  2.  Pindel
  3.  SvABA
  

This folder contains:
  1. Three  scripts:  	
  * BREAKDANCERscript.py
  * PINDELscript.py
  * SvABAscript.py
  2. Three submission scripts:  	
  * submitBREAKDANCERscript.py
  * submitPINDELscript.py
  * submitSvABAscript.py

## Dependencies:
This step makes use of the following software(s):
   * BREAKDANCER (http://breakdancer.sourceforge.net/)
   * PINDEL (http://gmt.genome.wustl.edu/packages/pindel/)
   * SvABA (https://github.com/walaj/svaba)
