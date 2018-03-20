
#!/bin/bash 

FILES=/mnt/flash/hb493/BWAMEM/VCpicard/*.vcf

for f in $FILES 
do 
        echo "Processing $f file..." 
        bgzip -c $f > $f.gz
	tabix -p vcf $f.gz
        cat $f 
done
