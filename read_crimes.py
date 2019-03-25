from geodist import *

def load_crimes(file_path):
	crime_csv = []
	with open(file_path, 'r') as file:
		for line in file:
			line = line.strip()
			line = line.split(',')
			crime_csv.append(line)
	return crime_csv


def concatenate(files):
	concatenated_files = []
	all_crimes = []
	all_crimes.append(load_crimes(files[0]))
	for file_path in files[1:]:
		loaded = load_crimes(files[0])
		del loaded[0]
		all_crimes.append(loaded)
	for file_rows in all_crimes:
		for row in file_rows:
			concatenated_files.append(row)
	return concatenated_files


def get_lat_lon(crime_data, postcode_lat_lon, radius):
    in_range = []
    for row in crime_data[1:]:
        if row[4] or row[5]:           
            lon = float(row[4].replace("−", "-"))
            lat = float(row[5].replace("−", "-"))
            kilometers = distance((lat, lon), postcode_lat_lon)
            # If a crime is within the radius to entire row is saved
            if kilometers <= radius:
                in_range.append(row)
    return in_range

files = ['Devon_and_Cornwall_crime_data_2018/2018-01-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-02-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-03-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-04-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-05-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-06-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-07-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-08-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-09-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-10-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-11-devon-and-cornwall-street.csv',
		 'Devon_and_Cornwall_crime_data_2018/2018-12-devon-and-cornwall-street.csv']


all_csv = concatenate(files)

