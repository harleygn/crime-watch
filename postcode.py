# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:30:11 2019

@author: Kalon Martin
"""
file_path = "C:/Users/Kalon Martin/Documents/GitHub/crime-watch/Devon_and_Cornwall_crime_data_2018/2018-01-devon-and-cornwall-street.csv"

def load_postcodes():
    with open(file_path , 'r' ) as file:
        for line in file:
            line.strip()
            
    return file

df = load_postcodes()