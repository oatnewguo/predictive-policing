import pandas as pd
#import csv

df = pd.read_csv('data\\stops\\raw\\los_angeles_ca_2010-2017.csv',
    usecols=['Stop Date', 'Sex Code', 'Descent Code'])
df.to_csv('data\\stops\\los_angeles_ca_2010-2017_extracted.csv')

descent_codes = list('ABCDFGHIJKLOPSUVWXZ')

'''
#All rows contain a valid descent code
for row, d in df['Descent Code'].iteritems():
    if d not in descent_codes:
        print('problem: ' + d)
'''

dfs_by_year = []
for i in range(8):
    dfs_by_year.append(df[df['Stop Date'].apply(lambda x: str(2010 + i)  in str(x))])

print("Year | White | Black | Hispanic")
year = 2010
for d in dfs_by_year:
    counts = d['Descent Code'].value_counts(normalize=True)
    print("{:<4}   {:<6.4}  {:<6.4}  {:<6.4}".format(year, counts.W, counts.B, counts.H))
    year += 1
'''
with open('data\\arrests\\raw\\los_angeles_ca_2010-2017.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if '2010' in row[2]:
            print('2010 spotted')
'''
