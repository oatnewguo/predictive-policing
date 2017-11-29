#input: year

mkdir -p $1/relfreq
join -t 0 $1/crime_trigrams_raw.txt $1/pp_trigrams_raw.txt | uniq > $1/relfreq/common_trigrams.tmp
join -t 0 $1/crime_trigrams_raw.txt $1/relfreq/common_trigrams.tmp | uniq -c > $1/relfreq/crime_tricounts.tmp
join -t 0 $1/pp_trigrams_raw.txt $1/relfreq/common_trigrams.tmp | uniq -c > $1/relfreq/pp_tricounts.tmp

#trigram | count in crime | count in pp
paste $1/relfreq/pp_tricounts.tmp $1/relfreq/crime_tricounts.tmp | awk '{print $2, $3, $4, $5, $1}' > $1/relfreq/trigram.txt

join -t 0 $1/crime_bigrams_raw.txt $1/pp_bigrams_raw.txt | uniq > $1/relfreq/common_bigrams.tmp
join -t 0 $1/crime_bigrams_raw.txt $1/relfreq/common_bigrams.tmp | uniq -c > $1/relfreq/crime_bicounts.tmp
join -t 0 $1/pp_bigrams_raw.txt $1/relfreq/common_bigrams.tmp | uniq -c > $1/relfreq/pp_bicounts.tmp

#bigram | count in crime | count in pp
paste $1/relfreq/pp_bicounts.tmp $1/relfreq/crime_bicounts.tmp | awk '{print $2, $3, $4, $1}' > $1/relfreq/bigram.txt