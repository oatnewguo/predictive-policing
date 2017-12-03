import sys
import re

def main(tokens_path):
    '''Cleans corpora that have been downloaded using LexisNexus and tokenized
        by Michelle.

    tokens_path - string path to .txt file containing tokenized corpus
    '''

    f = open(tokens_path, 'r+')
    text = f.read()
    text = re.sub('(\nof\ndocuments.*?length\nwords\n)', '', text, 1, flags=re.DOTALL)
    text = re.sub('(load\ndate\n.*?length\nwords\n)', '', text, flags=re.DOTALL)
    f.seek(0)
    f.truncate()
    f.write(text)
    f.close()

if __name__ == '__main__':
    error_message = 'Usage: clean.py <tokens_path.txt>'
    if len(sys.argv) < 2:
        sys.stderr.write(error_message)
    elif not (sys.argv[1].endswith('.txt')):
        sys.stderr.write(error_message)
    else:
        main(sys.argv[1])

    '''
    for i in range(2010, 2018):
        main(str(i)+'\\crime_tokens.txt')
        main(str(i)+'\\pp_tokens.txt')
    main('2010_2011\\tokens.txt')
    main('2012_2014\\tokens.txt')
    main('2015_2017\\tokens.txt')
    '''
