import userinput as ui
import postcode as pc

postcode, radius = ui.setup()

valid, index = pc.validate_postcode(postcode)

if valid:
    lat, long = pc.get_lat_long(index)
    print("Postcode: " + postcode + "\n" + "Latitude: " + lat + "\n" + "Longitude: " + long)
    
    print("Searching for crimes within " + str(radius) + "km of " + postcode + "...")

