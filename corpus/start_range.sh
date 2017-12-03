#!/bin/bash
#Generates unigram, bigram, trigram files given name of directory and corpus (must be same name)
#Example usage: sh start.sh 2010_2011 => 2010_2011 with uni/bi/trigram files
#Input: name of directory and corpus (must be same name)

mkdir -p $1
echo Creating n-gram files
tr -sc A-Za-z '\n' < $1/$1.txt | tr A-Z a-z > $1/tokens.txt
tail -n+2 $1/tokens.txt > $1/next.tmp
tail -n+3 $1/tokens.txt > $1/nextnext.tmp

cat $1/tokens.txt | sort | uniq -c | sort -rn > $1/unigrams.txt

echo Creating n-gram sorted
paste $1/tokens.txt $1/next.tmp $1/nextnext.tmp | sort > $1/trigrams_raw.txt
paste $1/tokens.txt $1/next.tmp | sort > $1/bigrams_raw.txt

echo Creating n-gram counts
paste $1/tokens.txt $1/next.tmp $1/nextnext.tmp | sort | uniq -c | sort -rn > $1/trigrams.txt
paste $1/tokens.txt $1/next.tmp | sort | uniq -c | sort -rn > $1/bigrams.txt

echo Creating uniq n-grams
paste $1/tokens.txt $1/next.tmp $1/nextnext.tmp | sort | uniq > $1/trigrams_uniq.txt
paste $1/tokens.txt $1/next.tmp | sort | uniq > $1/bigrams_uniq.txt