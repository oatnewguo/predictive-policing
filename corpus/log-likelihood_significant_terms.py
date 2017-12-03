'''This file was adapted from a file taken from the GitHub of Ted Dunning, creator of the log-
    likelihood score. It can be found here: https://github.com/tdunning/python-llr'''

import sys

from collections import Counter
import re

import llr

def count(files):
    '''Counts the words contained in a list of files'''
    words = []
    for file in files:
        with open(file) as f:
            words += re.findall('\w+', re.sub('[\r\n]', ' ', f.read()))
    words = [w.lower() for w in words]
    return Counter(words)

def main(focus_path, other_paths, output_path, num_terms=30):
    '''Finds the significant words in the text located at focus_path, compared
        with the rest of the corpus.

    focus_path - string path to .txt file to focus on
    other_paths - list of string paths to .txt files comprising the rest of the
        corpus
    output_path - string path to .txt file in which to write results
    num_terms - number of significant terms to show
    '''

    focus_text = count([focus_path])
    other_text = count(other_paths)

    diff = llr.llr_compare(focus_text, other_text)
    ranked = sorted(diff.items(), key=lambda x: x[1])

    with open(output_path, 'w') as output:
        for word, score in reversed(ranked[-num_terms:]):
            output.write('{:<20.10}   {}\n'.format(score, word))

if __name__ == '__main__':
    #main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    crime_tokens = ['2010\\crime_tokens.txt', '2011\\crime_tokens.txt', '2012\\crime_tokens.txt', '2013\\crime_tokens.txt', '2014\\crime_tokens.txt', '2015\\crime_tokens.txt', '2016\\crime_tokens.txt', '2017\\crime_tokens.txt']
    pp_tokens = ['2010\\pp_tokens.txt', '2011\\pp_tokens.txt', '2012\\pp_tokens.txt', '2013\\pp_tokens.txt', '2014\\pp_tokens.txt', '2015\\pp_tokens.txt', '2016\\pp_tokens.txt', '2017\\pp_tokens.txt']
    for i in range(8):
        main(crime_tokens[i], crime_tokens[:i] + crime_tokens[i+1:], '201'+str(i)+'\\crime_significant_terms.txt')
        main(pp_tokens[i], pp_tokens[:i] + pp_tokens[i+1:], '201'+str(i)+'\\pp_significant_terms.txt')

    main('2010_2011\\tokens.txt', ['2012_2014\\tokens.txt', '2015_2017\\tokens.txt'], '2010_2011\\significant_terms.txt')
    main('2012_2014\\tokens.txt', ['2015_2017\\tokens.txt', '2010_2011\\tokens.txt'], '2012_2014\\significant_terms.txt')
    main('2015_2017\\tokens.txt', ['2010_2011\\tokens.txt', '2012_2014\\tokens.txt'], '2015_2017\\significant_terms.txt')
