from geodist import *
import pandas as pd
import os


def load_crime_data(source_directory):
    """
    Loads crime data from multiple CSV files and joins them into one large
    dataset. The rows with missing lat/lon values are removed, and the index is
    reset.
    :param source_directory: a string containing a directory path
    :return: a dataframe of crime data
    """
    all_crimes = []
    # Lists all the files in the given directory
    crime_files = os.listdir(source_directory)
    # Builds a list containing the loaded CSVs
    for filename in crime_files:
        crime_dataframe = pd.read_csv(source_directory + filename)
        all_crimes.append(crime_dataframe)
    # Joins the loaded data into a single dataframe
    crimes = pd.concat(all_crimes)
    # Removes rows with a Null lat/lon value as these are useless to us
    crimes = crimes[pd.notnull(crimes['Longitude'])]
    crimes = crimes[pd.notnull(crimes['Latitude'])]
    # Resets indexes after concatenation so all indexes are unique
    crimes.reset_index(drop=True, inplace=True)
    return crimes


def check_crime_radius(crime_data, postcode_lat_lon, radius):
    """
    Takes a dataframe of crime data and finds crimes within a given radius of a
    given postcode lat/lon.
    :param crime_data: a dataframe of crime data
    :param postcode_lat_lon: a two-element array containing a lat and lon value
    :param radius: an integer or float value for the radius size, in KM
    :return: a dataframe containing all crimes recorded within the radius, if
             there are no results, a None is returned
    """
    in_range = []
    # Finds the distance between each crime and the postcode using geodist.py
    for row in range(len(crime_data)):
        kilometers = distance([crime_data.iat[row, 5], crime_data.iat[row, 4]],
                              postcode_lat_lon)
        # If a crime is within the radius to entire row is saved
        if kilometers <= radius:
            in_range.append(crime_data.loc[[row]])
    # Concatenates the rows into a single dataframe if there is more than one
    if len(in_range) >= 2:
        return pd.concat(in_range)
    # if there is only one result, concatenation is not required, so the first
    # and only result is returned
    elif len(in_range) == 1:
        return in_range[0]
    # If there are no results a None will be returned
