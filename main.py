import userinput as ui
import postcode as pc
import read_crimes as cr

postcode, radius = ui.setup()

valid, index = pc.validate_postcode(postcode)

if valid:
    lat_long = pc.get_lat_long(index)
    crime_data = cr.get_lat_lon(cr.all_csv, lat_long, int(radius))
    
    print("Searching for crime data within " + str(radius) + "km of " + postcode + "...")
    