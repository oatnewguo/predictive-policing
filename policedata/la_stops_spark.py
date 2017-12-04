import pyspark
from pyspark.sql import SQLContext

#open up a spark context
sc = pyspark.SparkContext()
# Open an sql context
sqlContext = pyspark.sql.SQLContext(sc)

#Load in the CSV
df = sqlContext.read.format("csv").option("header", "true").load("Stop_Data_from_2010_to_Present.csv")

# List of columns to keep
keep_list = ['Stop Date', 'Sex Code', 'Descent Code']

# Filter out the columns we dont need
df = df.select([column for column in df.columns if column in keep_list])

#Create a clean CSV with desired columns
#df.write.csv('mycsv.csv')

descent_codes = list('ABCDFGHIJKLOPSUVWXZ')

#Create a code list of all the codes in the file
codeList = df.select("Descent Code").rdd.flatMap(lambda x: x).collect()
api_codes = list('ACDFGJKLPSUVZ')

countW =0
countB = 0
countH = 0
countA = 0
total = 0
for p in codeList:
    if p == 'W':
        countW +=1
    elif p == 'B':
        countB += 1
    elif p =='H':
        countH += 1
    elif p in api_codes:
        countA += 1
    total += 1

print("White | Black | Hispanic | Asian | Total")
print("{:<7} {:<7} {:<7}    {:<7} {}".format(countW, countB, countH, countA, total))
