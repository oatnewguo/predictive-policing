from stops import *

def main():
    stops_df = Stops()
    stops_df.add_LosAngeles('data\\stops\\raw\\los_angeles_ca_2010-2017.csv')
    #stops_df.add_SanFrancisco(['data\\stops\\raw\\san_francisco_ca_2014.csv', 'data\\stops\\raw\\san_francisco_ca_2015.csv', 'data\\stops\\raw\\san_francisco_ca_2016.csv'])
    stops_df.pickle('stops.pkl')

if __name__ == '__main__':
    main()
