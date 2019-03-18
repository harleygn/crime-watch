import re
from tkinter import *

def setup():
    valid = False

    while valid == False:
        print("Enter a postcode...")
        postcode = input()
        if re.search("^\w\w\w \w\w\w$", postcode) is not None:
            valid = True
        else:
            print("Please enter postcode in the correct format e.g. AB1 3CD.")

    valid = False

    while valid == False:
        print("Enter a radius...")
        radius = input()
        if int(radius) <= 5:
            valid = True
        else:
            print("Please enter a NUMBER between 1 and 5.")

    return postcode, radius



