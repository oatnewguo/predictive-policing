#!/bin/bash
#Generates unigram, bigram, trigram files given a year to parse from c_LexisNexis
#Example usage: sh start.sh 2010 => directory 2010 with uni/bi/trigram files
#Input: year (ex. 2010) or 'allyears'

mkdir -p $1
echo Creating n-gram files for general crime corpus
tr -sc A-Za-z '\n' < c_LexisNexis/LAcrime_$1.txt | tr A-Z a-z > $1/crime_tokens.txt
tail -n+2 $1/crime_tokens.txt > $1/next.tmp
tail -n+3 $1/crime_tokens.txt > $1/nextnext.tmp

cat $1/crime_tokens.txt | sort | uniq -c | sort -rn > $1/crime_unigrams.txt

echo Creating n-gram sorted
paste $1/crime_tokens.txt $1/next.tmp $1/nextnext.tmp | sort > $1/crime_trigrams_raw.txt
paste $1/crime_tokens.txt $1/next.tmp | sort > $1/crime_bigrams_raw.txt

echo Creating n-gram counts
paste $1/crime_tokens.txt $1/next.tmp $1/nextnext.tmp | sort | uniq -c | sort -rn > $1/crime_trigrams.txt
paste $1/crime_tokens.txt $1/next.tmp | sort | uniq -c | sort -rn > $1/crime_bigrams.txt

echo Creating uniq n-grams
paste $1/crime_tokens.txt $1/next.tmp $1/nextnext.tmp | sort | uniq > $1/crime_trigrams_uniq.txt
paste $1/crime_tokens.txt $1/next.tmp | sort | uniq > $1/crime_bigrams_uniq.txt


echo Creating n-gram files for predpol corpus
tr -sc A-Za-z '\n' < c_LexisNexis/LAprepol_$1.txt | tr A-Z a-z > $1/pp_tokens.txt
tail -n+2 $1/pp_tokens.txt > $1/next.tmp
tail -n+3 $1/pp_tokens.txt > $1/nextnext.tmp

cat $1/pp_tokens.txt | sort | uniq -c | sort -rn > $1/pp_unigrams.txt

echo Creating n-gram sorted
paste $1/pp_tokens.txt $1/next.tmp $1/nextnext.tmp | sort > $1/pp_trigrams_raw.txt
paste $1/pp_tokens.txt $1/next.tmp | sort > $1/pp_bigrams_raw.txt

echo Creating n-gram counts
paste $1/pp_tokens.txt $1/next.tmp $1/nextnext.tmp | sort | uniq -c | sort -rn > $1/pp_trigrams.txt
paste $1/pp_tokens.txt $1/next.tmp | sort | uniq -c | sort -rn > $1/pp_bigrams.txt

echo Creating uniq n-grams
paste $1/pp_tokens.txt $1/next.tmp $1/nextnext.tmp | sort | uniq > $1/pp_trigrams_uniq.txt
paste $1/pp_tokens.txt $1/next.tmp | sort | uniq > $1/pp_bigrams_uniq.txt