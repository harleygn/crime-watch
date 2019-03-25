from postcode import validate_postcode
from tkinter import *

def setup():
    valid = False
    radius_inputs = [1,2,50]

    while valid == False:
        print("Enter a postcode...")
        postcode = input()
        postcode = postcode.upper()
        
        if validate_postcode(postcode)[0]:
            valid = True
        else:
            print("Invalid postcode. Please enter in a valid format e.g. AB1 2CD or EG11 2EG")
            
    valid = False

    while valid == False:
        print("Enter a radius...")
        radius = input()
        if int(radius) in radius_inputs:
            valid = True
        else:
            print("Please enter a valid radius (1 , 2 , 5)")

    return postcode, radius

