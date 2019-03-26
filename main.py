'''
Created on Tue Mar 19 12:30:18 2019

@author: Kalon Martin

'''

import userinput as ui
import postcode as pc
import read_crimes as cr
import report as re
import save_report as sr

postcode, radius = ui.setup()

valid, index = pc.validate_postcode(postcode)

if valid:
    print("Searching for crime data within " + str(radius) + "km of " + postcode + "...")
    lat_long = pc.get_lat_long(index)
    crime_data = cr.get_lat_lon(cr.all_csv, lat_long, int(radius))
    
    sr.save(re.create_report_data(crime_data), r'./')
