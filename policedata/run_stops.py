from stops import *

def main():
    stops_df = Stops('stops.csv')

    #stops_df.add_LosAngeles('data\\stops\\raw\\los_angeles_ca_2010-2017.csv')
    #stops_df.add_Burlington('data\\stops\\raw\\burlington_vt_2011-2017.csv')
    #stops_df.add_SanFrancisco(['data\\stops\\raw\\san_francisco_ca_2014.csv', 'data\\stops\\raw\\san_francisco_ca_2015.csv', 'data\\stops\\raw\\san_francisco_ca_2016.csv'])
    #stops_df.to_csv('stops.csv')
    stops_df.show_counts('Burlington', 2011, 2017)
    stops_df.show_percents('Burlington', 2011, 2017)

if __name__ == '__main__':
    main()
