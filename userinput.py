import re

def setup():
    valid = False
    while valid == False:
        print("Enter a postcode...")
        postcode = input()
        if re.search("^\w\w\w \w\w\w$", postcode) is not None:
            valid = True

    print("Enter a radius...")
    radius = input()

    return postcode, radius



