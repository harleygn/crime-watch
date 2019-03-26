'''
Created on Tue Mar 19 12:30:18 2019

@author: Kalon Martin

'''

#import all module dependencies
import userinput as ui
import postcode as pc
import read_crimes as cr
import report as re
import save_report as sr
import os

postcode, radius = ui.setup()

valid, index = pc.validate_postcode(postcode)

#when the postcode is valid
if valid:
    print("Searching for crime data within " + str(radius) + "km of " + postcode + "...")
    print(os.getcwd())
    lat_long = pc.get_lat_long(index)
    crime_data = cr.get_lat_lon(cr.all_csv, lat_long, int(radius))

    #save the report from the crime data list.
    sr.save(re.create_report_data(crime_data), os.getcwd() + r"\Scripts\Reports")

