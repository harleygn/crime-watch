import userinput as ui
import postcode as pc
import read_crimes as cr

postcode, radius = ui.setup()

valid, index = pc.validate_postcode(postcode)

if valid:
    lat_long = pc.get_lat_long(index)
    crime_data = cr.load_crimes("./Documents/Devon_and_Cornwall_crime_data_2018")
    result_data = cr.check_crime_radius(crime_data, lat_long, radius)
    
    print("Postcode: " + postcode + "\n" + "Latitude: " + lat_long[0] + "\n" + "Longitude: " + lat_long[1])
    
    print("Searching for crimes within " + str(radius) + "km of " + postcode + "...")

