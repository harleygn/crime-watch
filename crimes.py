# import geodist
import pandas as pd
import os


def load_crime_data(source_directory):
    crime_files = os.listdir(source_directory)
    all_crimes = []
    for filename in crime_files:
        crime_dataframe = pd.read_csv(source_directory + filename)
        all_crimes.append(crime_dataframe)
    crimes = pd.concat(all_crimes)
    crimes = crimes[pd.notnull(crimes['Longitude'])]
    crimes = crimes[pd.notnull(crimes['Latitude'])]
    return crimes


def get_lat_lon(dataframe):
    return dataframe[['Longitude', 'Latitude']]


print(get_lat_lon(load_crime_data('Devon_and_Cornwall_crime_data_2018/')))
