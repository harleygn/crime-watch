from geodist import *
import os
dirname = os.path.dirname(__file__)

def load_crimes(file_path):
	"""

	:param file_path:
	:return:
	"""
	crime_csv = []
	with open(file_path, 'r') as file:
		for line in file:
			line = line.strip()
			line = line.split(',')
			crime_csv.append(line)
	return crime_csv


def concatenate(files):
	"""

	:param files:
	:return:
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
    for row in crime_data[1:]:
        count += 1
        
        if row[4] or row[5]:           
            lon = float(row[4].replace("−", "-"))
            lat = float(row[5].replace("−", "-"))
            kilometers = distance((lat, lon), postcode_lat_lon)
            # If a crime is within the radius to entire row is saved
            if kilometers <= radius:
                in_range.append(row)
                
        #percentage for user
        if(round(((len(crime_data) - (len(crime_data) - count)) / len(crime_data)) * 100) > percentage):        
            percentage += 25
            print(str(percentage) + "%")
            
    return in_range

files = [os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-01-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-02-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-03-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-04-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-05-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-06-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-07-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-08-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-09-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-10-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-11-devon-and-cornwall-street.csv'),
		 os.path.join(dirname, './Devon_and_Cornwall_crime_data_2018/2018-12-devon-and-cornwall-street.csv'),]


all_csv = concatenate(files)
