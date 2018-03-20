
#!/bin/bash 

FILES=*.fastq

for f in $FILES 
do 
        echo "Processing $f file..." 
        sed 's/K/J/g' $f > $f.newq.fastq &
done
