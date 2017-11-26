import csv
import io

f = open('data\\stops\\raw\\los_angeles_ca_2010-2017.csv','r')
fileObject = csv.reader(f)
row_count = sum(1 for row in fileObject)
print(row_count)
