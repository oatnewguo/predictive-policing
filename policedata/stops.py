import pandas as pd

class Stops:

    def __init__(self, file_path=None):
        '''Initialize object with a pandas DataFrame. If file_path is given,
            load an existing DataFrame; if not, create a new one.

        file_path - path to .csv file containing csv of existing DataFrame.
        '''

        if file_path == None:
            self.df = pd.DataFrame(columns = ['City', 'Date', 'Race', 'Gender'])
        else:
            self.df = pd.read_csv(file_path, parse_dates=['Date'])

        self.race_codes = list('ABCDFGHIJKLOPSUVWXZ')

    def to_csv(self, output_path):
        '''Write contents of self.df as a .csv file.'''

        self.df.to_csv(output_path)

    def add_LosAngeles(self, file_path):
        '''Append Los Angeles, CA data from file to self.df.

        file_path - .csv file containing data from Los Angeles.
        '''

        load_df = pd.read_csv(file_path,
            usecols=['Stop Date', 'Sex Code', 'Descent Code'], parse_dates=['Stop Date'], infer_datetime_format=True)
        load_df.insert(0, 'City', 'Los Angeles')
        load_df.columns = ['City', 'Gender', 'Race', 'Date']
        load_df = load_df[['City', 'Date', 'Race', 'Gender']]

        race_codes = {'C': 'A', 'D': 'A', 'F': 'A', 'G': 'A', 'J': 'A',
            'K': 'A', 'L': 'A', 'P': 'A', 'S': 'A', 'U': 'A', 'V': 'A', 'Z': 'A'}
        load_df['Race'] = load_df['Race'].replace(to_replace=list(race_codes.keys()), value=list(race_codes.values()))

        self.df = self.df[self.df['City'] != 'Los Angeles']
        self.df = self.df.append(load_df)

    def add_SanFrancisco(self, file_paths):
        '''Append San Francisco, CA data from file to self.df.

        file_paths - list of .csv files containing data from San Francisco.
        '''

        load_df = pd.DataFrame(columns=['Date of Stop', 'Race', 'Sex'])
        for csv in file_paths:
            load_df = load_df.append(pd.read_csv(csv,
                usecols=['Date of Stop', 'Race', 'Sex'], parse_dates=['Date of Stop'], infer_datetime_format=True))
        load_df.insert(0, 'City', 'San Francisco')
        load_df.columns = ['City', 'Date', 'Race', 'Gender']

        self.df = self.df[self.df['City'] != 'San Francisco']
        self.df = self.df.append(load_df)

    def add_Burlington(self, file_path):
        '''Append Burlington, VT data from file to self.df.

        file_path - .csv file containing data from Burlington.
        '''

        load_df = pd.read_csv(file_path,
            usecols=['Gender', 'Date Issued', 'Race'], parse_dates=['Date Issued'], infer_datetime_format=True)
        load_df.insert(0, 'City', 'Burlington')
        load_df.columns = ['City', 'Gender', 'Date', 'Race']
        load_df = load_df[['City', 'Date', 'Race', 'Gender']]

        race_codes = {'White - W': 'W', 'Black - B': 'B', 'Hispanic - H': 'H',
            'Asian - A': 'A', 'Pacific Is - A': 'A', 'W=White': 'W',
            'B=Black': 'B', 'H=Hispanic': 'H', 'A=Asian/ (Pac.Island)': 'A'}
        gender_codes = {'Male - M': 'M', 'Female - F': 'F'}
        load_df['Race'] = load_df['Race'].replace(to_replace=list(race_codes.keys()), value=list(race_codes.values()))
        load_df['Gender'] = load_df['Gender'].replace(to_replace=list(gender_codes.keys()), value=list(gender_codes.values()))

        self.df = self.df[self.df['City'] != 'Burlington']
        self.df = self.df.append(load_df)

    def show_percents(self, city, start_year, end_year):
        '''Show percents of stops for whites, blacks, and Hispanics in a given
            city by year over a range of years.

        city - string name of city
        start_year - int first year to show data for
        end_year - int last year to show data for
        '''

        print("Year | White | Black | Hispanic | Asian")
        for year in range(start_year, end_year+1):
            year_df = self.df[(self.df['City']==city) & (self.df['Date'].dt.year == year)]
            counts = year_df['Race'].value_counts(normalize=True)
            counts_list = []
            if 'W' in counts:
                counts_list.append(counts.W)
            else:
                counts_list.append(0.)
            if 'B' in counts:
                counts_list.append(counts.B)
            else:
                counts_list.append(0.)
            if 'H' in counts:
                counts_list.append(counts.H)
            else:
                counts_list.append(0.)
            if 'A' in counts:
                counts_list.append(counts.A)
            else:
                counts_list.append(0.)
            print("{:<4}   {:<6.6}  {:<6.6}  {:<6.6}     {:<6.6}".format(year, str(counts_list[0]), str(counts_list[1]), str(counts_list[2]), str(counts_list[3])))

    def show_counts(self, city, start_year, end_year):
        '''Show counts of stops for whites, blacks, Hispanics, and total in a
            given city by year over a range of years.

        city - string name of city
        start_year - int first year to show data for
        end_year - int last year to show data for
        '''

        print("Year | White | Black | Hispanic | Asian | Total")
        for year in range(start_year, end_year+1):
            year_df = self.df[(self.df['City']==city) & (self.df['Date'].dt.year == year)]
            counts = year_df['Race'].value_counts()
            counts_list = []
            if 'W' in counts:
                counts_list.append(counts.W)
            else:
                counts_list.append(0)
            if 'B' in counts:
                counts_list.append(counts.B)
            else:
                counts_list.append(0)
            if 'H' in counts:
                counts_list.append(counts.H)
            else:
                counts_list.append(0)
            if 'A' in counts:
                counts_list.append(counts.A)
            else:
                counts_list.append(0)
            print("{:<4}   {:<7} {:<7} {:<7}    {:<7} {}".format(year, counts_list[0], counts_list[1], counts_list[2], counts_list[3], year_df.shape[0]))
