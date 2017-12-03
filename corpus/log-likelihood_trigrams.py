import nltk
from nltk.collocations import *
import sys

def main(text_path, output_path):
    '''Generates trigram collocations, ordered by their Dunning's log-likelihood
        score, from a text.

    text_path - string path to .txt input file
    output_path - string path to .txt file for outputting trigrams
    '''

    document = open(text_path, 'r')
    raw = document.read()
    document.close()

    words = nltk.word_tokenize(raw)

    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    finder = TrigramCollocationFinder.from_words(words)
    trigrams = finder.score_ngrams(trigram_measures.likelihood_ratio)

    results = open(output_path, 'w')
    freq_dist = finder.ngram_fd
    for (word1, word2, word3), score in trigrams:
        results.write('{:<20.10}   {:<9}   {} {} {} \n'.format(score,
            freq_dist[word1, word2, word3], word1, word2, word3))
    results.close()

if __name__ == '__main__':
    '''
    error_message = 'Usage: log-likelihood_trigrams.py <text_path.txt> <output_path.txt>'
    if len(sys.argv) < 3:
        sys.stderr.write(error_message)
    elif not (sys.argv[1].endswith('.txt') and sys.argv[2].endswith('.txt')):
        sys.stderr.write(error_message)
    else:
        main(sys.argv[1], sys.argv[2])

    '''
    for i in range(2010, 2018):
        main(str(i)+'\\crime_tokens.txt', str(i)+'\\crime_trigrams_ll.txt')
        main(str(i)+'\\pp_tokens.txt', str(i)+'\\pp_trigrams_ll.txt')
    main('2010_2011\\tokens.txt', '2010_2011\\trigrams_ll.txt')
    main('2012_2014\\tokens.txt', '2012_2014\\trigrams_ll.txt')
    main('2015_2017\\tokens.txt', '2015_2017\\trigrams_ll.txt')
