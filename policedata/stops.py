import pandas as pd
#import csv

class Stops:

    def __init__(self, pickle_file_path=None):
        '''Initialize object with a pandas DataFrame. If pickle_file_path is
            given, load an existing DataFrame; if not, create a new one.

        pickle_file_path - path to .pkl file containing pickle of existing DataFrame.
        '''

        if pickle_file_path == None:
            self.df = pd.DataFrame(columns = ['City', 'Date', 'Race', 'Gender'])
        else:
            self.df = pd.read_pickle(pickle_file_path)

        self.race_codes = list('ABCDFGHIJKLOPSUVWXZ')

    def pickle(self, pickle_file_path):
        '''Store self.df as a .pkl file.'''

        self.df.to_pickle(pickle_file_path)

    def add_LosAngeles(self, file_path):
        '''Append Los Angeles, CA data from file to self.df.

        file_path - .csv file containing data from Los Angeles.
        '''

        load_df = pd.read_csv(file_path,
            usecols=['Stop Date', 'Sex Code', 'Descent Code'], parse_dates=['Stop Date'], nrows = 5000000)
        print('done')
        load_df.insert(0, 'City', 'Los Angeles')
        print('done')
        load_df.columns = ['City', 'Gender', 'Race', 'Date']
        print('done')
        load_df = load_df[['City', 'Date', 'Race', '']]
        print('done')
        self.df = self.df[not self.df.city.str == 'Los Angeles']
        print('done')
        self.df = self.df.append(load_df)
        print('done')

    def add_SanFrancisco(self, file_paths):
        '''Append San Francisco, CA data from file to self.df.

        file_paths - list of .csv files containing data from San Francisco.
        '''

        load_df = pd.DataFrame(columns=['Date of Stop', 'Race', 'Sex'])
        for csv in file_paths:
            load_df = load_df.append(pd.read_csv(csv,
                usecols=['Date of Stop', 'Race', 'Sex'], parse_dates=['Date of Stop']), nrows=1000000)
        load_df.insert(0, 'City', 'San Francisco')
        load_df.columns = ['City', 'Date', 'Race', '']

        self.df = self.df[not self.df.city.str == 'San Francisco']
        self.df = self.df.append(load_df)

    def add_Burlington(self, file_path):
        '''Append Burlington, VT data from file to self.df.

        file_path - .csv file containing data from Burlington.
        '''

        load_df = pd.read_csv(file_path,
            usecols=['Gender', 'Date Issued', 'Race'], parse_dates=['Date Issued'])
        load_df.insert(0, 'City', 'Burlington')
        load_df.columns = ['City', 'Gender', 'Date', 'Race']
        load_df = load_df[['City', 'Date', 'Race', 'Gender']]

        self.df = self.df[not self.df.city.str == 'Burlington']
        self.df = self.df.append(load_df)

    '''
    def display(self):
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
