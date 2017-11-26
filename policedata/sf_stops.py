import pandas as pd

dfs_by_year = []
dfs_by_year.append(pd.read_csv('data\\stops\\raw\\san_francisco_ca_2014.csv',
    usecols=['Date of Stop', 'Race', 'Sex', 'District']))
dfs_by_year.append(pd.read_csv('data\\stops\\raw\\san_francisco_ca_2015.csv',
    usecols=['Date of Stop', 'Race', 'Sex', 'District']))
dfs_by_year.append(pd.read_csv('data\\stops\\raw\\san_francisco_ca_2016.csv',
    usecols=['Date of Stop', 'Race', 'Sex', 'District']))

print("Year | White | Black | Hispanic")
year = 2014
for d in dfs_by_year:
    counts = d['Race'].value_counts(normalize=True)
    print("{:<4}   {:<6.4}  {:<6.4}  {:<6.4}".format(year, counts.W, counts.B, counts.H))
    year += 1
'''
with open('data\\arrests\\raw\\los_angeles_ca_2010-2017.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if '2010' in row[2]:
            print('2010 spotted')
'''
