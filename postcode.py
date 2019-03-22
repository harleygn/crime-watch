# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:30:11 2019

@author: Kalon Martin
"""

file_path = "C:/Users/Kalon Martin/Documents/GitHub/crime-watch/postcodes.csv"

def load_postcodes():
    '''
    This function reduces the size of the original CSV and gathers the information needed. This is postcode, Latitude, and Longitude.
    :return return_list: - This return the list that holds the postcode, latitude, and longitude all separated by a comma.
    '''
    csv = []
    return_list = []
    
    with open(file_path, 'r') as file:   # This reads the CSV, and names it 'file'.
        for line in file:
            line = line.strip()# Strips the white-space from the imported words.
            line = line.split(',')# Strips the data into key elements needed.
            csv.append(line)
    
    for i in range(len(csv)):# Find the length of the CSV
        #starts at above 0 to delete the column titles
        if i > 0:
            csv_list = csv[i]
            temp_list = []
            temp_list.append(csv_list[0].strip('\"'))# Appends the first row inthe table (Postcode)
            temp_list.append(csv_list[10].strip('\"'))#Appends the 10th row in the table (Latitude)
            temp_list.append(csv_list[11].strip('\"'))#Appends the 11th row in the table (longitude)
            
            return_list.append(temp_list)
        
    return return_list

def validate_postcode(postcode):
    '''
    This function validates the postcodes, given by the user input, against the CSV file created created from all the different CSVs.
    :param postcode: - A string from user input module.
    :return: This returns an boolean True or Flase for whether the postcode is valid
    :return: This will give an index depending on if the postcode is valid
    '''
    valid = False
    count = 0
    
    while valid == False:
        temp_list = postcode_df[count]# This counts the occurences of the substring
        if count < len(postcode_df) - 1:
            
            if postcode == temp_list[0]:               
                valid = True
                index = count
                break
        else:
            index = 0
            break
        
        count += 1
    
    return valid, index

def get_lat_long(index):
    '''
    This function gets the latitude and longitude from the data frame.
    :param index: The row of the latitude and longitude in the data frame
    :return: This will return the latitude and longitude of the postcode
    '''
    lat = postcode_df[index][1]
    long = postcode_df[index][2]
    
    return lat, long

postcode_df = load_postcodes()    
        
