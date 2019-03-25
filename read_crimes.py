from geodist import *


def load_crimes(file_path):
	"""
	Loads the data from a given CSV file into an array
	:param file_path: filepath and name of CSV file
	:return: an array containing each row and column of the CSV
	"""
	crime_csv = []
	# Opens the file for operation
	with open(file_path, 'r') as file:
		# Reads each row, removes newline characters
		for line in file:
			line = line.strip()
			# Separates columns at the comma delimiter
			line = line.split(',')
			# The resulting list is added to a list of all the rows
			crime_csv.append(line)
	return crime_csv


def concatenate(files):
	"""
	Joins multiple arrays into one, preserving the headers for the first only
	:param files: A list containing all the loaded array data
	:return: An array containing all the data in a single object
	"""
	concatenated_files = []
	# Loads the whole of the first file, including headers
	all_crimes = [load_crimes(files[0])]
	# Skips first file as already loaded
	for file_path in files[1:]:
		loaded = load_crimes(files[0])
		# Removes header as this would be repeated otherwise
		del loaded[0]
		all_crimes.append(loaded)
	# Adds all the rows from all the files into a single list
	for file_rows in all_crimes:
		for row in file_rows:
			concatenated_files.append(row)
	return concatenated_files


def get_lat_lon(crime_data, postcode_lat_lon, radius):
    in_range = []
    count = 0
    percentage = 0
	# Skips the header row
    for row in crime_data[1:]:
        count += 1
		# Only reads rows that have data present in the lon/lat columns
        if row[4] or row[5]:
			# Replaces dashes with ones that the float function recognises
            lon = float(row[4].replace("−", "-"))
            lat = float(row[5].replace("−", "-"))
            kilometers = distance((lat, lon), postcode_lat_lon)
            # Saves a crime record if it is in range
            if kilometers <= radius:
                in_range.append(row)
        # Displays completion percentage to user
        if round(((len(crime_data) - (len(crime_data) - count)) /
				  len(crime_data)) * 100) > percentage:
            percentage += 25
            print(str(percentage) + "%")
    return in_range


# Locations of CSV files
files = [
	'Devon_and_Cornwall_crime_data_2018/2018-01-devon-and-cornwall-street.csv',
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
