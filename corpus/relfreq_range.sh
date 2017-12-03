#input: 2 year ranges i.e. 2010_2011 2012_2014

mkdir -p relfreq
join -t 0 $1/trigrams_raw.txt $2/trigrams_raw.txt | uniq > relfreq/common_trigrams.tmp
join -t 0 $1/trigrams_raw.txt relfreq/common_trigrams.tmp | uniq -c > relfreq/tricounts_$1.tmp
join -t 0 $2/trigrams_raw.txt relfreq/common_trigrams.tmp | uniq -c > relfreq/tricounts_$2.tmp

#trigram | count in crime | count in pp
paste relfreq/tricounts_$1.tmp relfreq/tricounts_$2.tmp | awk '{print $2, $3, $4, $5, $1}' > relfreq/$1_vs_$2_trigram.txt

join -t 0 $1/bigrams_raw.txt $2/bigrams_raw.txt | uniq > relfreq/common_bigrams.tmp
join -t 0 $1/bigrams_raw.txt relfreq/common_bigrams.tmp | uniq -c > relfreq/bicounts_$1.tmp
join -t 0 $2/bigrams_raw.txt relfreq/common_bigrams.tmp | uniq -c > relfreq/bicounts_$2.tmp

#bigram | count in crime | count in pp
paste relfreq/bicounts_$1.tmp relfreq/bicounts_$2.tmp | awk '{print $2, $3, $4, $1}' > relfreq/$1_vs_$2_bigram.txt