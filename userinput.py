import re
from postcode import validate_postcode
from tkinter import *

def setup():
    valid = False

    while valid == False:
        print("Enter a postcode...")
        postcode = input()
        
        if validate_postcode(postcode)[0]:
            valid = True
        else:
            print("Invalid postcode.")
            
    valid = False

    while valid == False:
        print("Enter a radius...")
        radius = input()
        if int(radius) <= 5:
            valid = True
        else:
            print("Please enter a NUMBER between 1 and 5.")

    return postcode.upper(), radius

