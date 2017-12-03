import nltk
from nltk.collocations import *
import sys

def main(text_path, output_path):
    '''Generates bigram collocations, ordered by their Dunning's log-likelihood
        score, from a text.

    text_path - string path to .txt input file
    output_path - string path to .txt file for outputting bigrams
    '''

    document = open(text_path, 'r')
    raw = document.read()
    document.close()

    words = nltk.word_tokenize(raw)

    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(words)
    bigrams = finder.score_ngrams(bigram_measures.likelihood_ratio)

    results = open(output_path, 'w')
    freq_dist = finder.ngram_fd
    for (word1, word2), score in bigrams:
        results.write('{:<20.10}   {:<9}   {} {} \n'.format(score,
            freq_dist[word1, word2], word1, word2))
    results.close()

if __name__ == '__main__':
    error_message = 'Usage: log-likelihood.py <text_path.txt> <output_path.txt>'
    if len(sys.argv) < 3:
        sys.stderr.write(error_message)
    elif not (sys.argv[1].endswith('.txt') and sys.argv[2].endswith('.txt')):
        sys.stderr.write(error_message)
    else:
        main(sys.argv[1], sys.argv[2])

    '''
    for i in range(2010, 2018):
        main(str(i)+'\\crime_tokens.txt', str(i)+'\\crime_bigrams_ll.txt')
        main(str(i)+'\\pp_tokens.txt', str(i)+'\\pp_bigrams_ll.txt')
    main('2010_2011\\tokens.txt', '2010_2011\\bigrams_ll.txt')
    main('2012_2014\\tokens.txt', '2012_2014\\bigrams_ll.txt')
    main('2015_2017\\tokens.txt', '2015_2017\\bigrams_ll.txt')
    '''
