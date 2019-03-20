# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:30:11 2019

@author: Kalon Martin
"""
file_path = "C:/Users/Kalon Martin/Documents/GitHub/crime-watch/postcodes.csv"

def load_postcodes():
    csv = []
    return_list = []
    
    with open(file_path, 'r') as file:      
        for line in file:
            line = line.strip()
            line = line.split(',')
            csv.append(line)
    
    for i in range(len(csv)):
        #starts at above 0 to delete the column titles
        if i > 0:
            csv_list = csv[i]
            temp_list = []
            temp_list.append(csv_list[0].strip('\"'))
            temp_list.append(csv_list[10].strip('\"'))
            temp_list.append(csv_list[11].strip('\"'))
            
            return_list.append(temp_list)
        
    return return_list

def validate_postcode(postcode):  
    valid = False
    count = 0
    
    while valid == False:
        temp_list = postcode_df[count]
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
    lat = postcode_df[index][1]
    long = postcode_df[index][2]
    
    return lat, long

postcode_df = load_postcodes()    
        
        