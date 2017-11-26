import pandas as pd
#import csv

df = pd.read_csv('data\\arrests\\raw\\los_angeles_ca_2010-2017.csv',
    usecols=['Arrest Date', 'Area ID', 'Sex Code', 'Descent Code'])
#df.to_csv('data\\arrests\\los_angeles_ca_2010-2017.csv')

descent_codes = list('ABCDFGHIJKLOPSUVWXZ')

'''
#All rows contain a valid descent code
for row, d in df['Descent Code'].iteritems():
    if d not in descent_codes:
        print('problem: ' + d)
'''

dfs_by_year = []
for i in range(8):
    dfs_by_year.append(df[df['Arrest Date'].apply(lambda x: str(2010 + i)  in str(x))])

print("Year | White | Black | Hispanic")
year = 2010
for d in dfs_by_year:
    counts = d['Descent Code'].value_counts(normalize=True)
    print("{:<4}   {:<6.4}  {:<6.4}  {:<6.4}".format(year, counts.W, counts.B, counts.H))
    year += 1
'''
#print("Year | Central | Rampart | Southwest | Hollenbeck | Harbor | Hollywood | Wilshire | West LA | Van Nuys | West Valley | Northeast | 77th Street | Newton | Pacific | North Hollywood | Foothill | Devonshire | Southeast | Mission | Olympic | Topanga")
year = 2010
for d in dfs_by_year:
    counts = d['Area ID'].value_counts(normalize=True)
    #print("{:<4} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3} {:<4.3}".format(year, counts.1, counts.2, counts.3, counts.4, counts.5, counts.6, counts.7, counts.8, counts.9, counts.10, counts.11, counts.12, counts.13, counts.14, counts.15, counts.16, counts.17, counts.18, counts.19, counts.20, counts.21))
    print(str(counts.1))
    year += 1
'''

'''
with open('data\\arrests\\raw\\los_angeles_ca_2010-2017.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if '2010' in row[2]:
            print('2010 spotted')
'''
