from geodist import *
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
    # Resets indexes after concatenation so all indexes are unique
    crimes.reset_index(drop=True, inplace=True)
    return crimes


def check_crime_radius(crime_data, postcode_lat_lon, radius):
    in_range = []
    for row in range(len(crime_data)):
        kilometers = distance([crime_data.iat[row, 5], crime_data.iat[row, 4]],
                              [50.71527036, -2.44427954])
        if kilometers <= radius:
            in_range.append(crime_data.loc[[row]])
    if len(in_range) >= 2:
        return pd.concat(in_range)
    elif len(in_range) == 1:
        return in_range[0]


sample_pc = [50.71527036, -2.44427954]

crimes = load_crime_data('Devon_and_Cornwall_crime_data_2018/')
print(check_crime_radius(crimes, sample_pc, 50))
