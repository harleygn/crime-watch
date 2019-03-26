from postcode import validate_postcode

def setup():
    '''
    A function that allows for the initial set up of the program. It asks the user for a "POSTCODE" and a "RADIUS".
    It then validates both the postcode and the radius before the program moves on.
    :return: postcode - a string value containing a valid postcode.
    :return: radius - a string value containing a valid radius.
    '''
    valid = False
    radius_inputs = [1, 2, 5]

    while not valid:
        print("Enter a postcode...")
        postcode = input()
        postcode = postcode.upper()
        if "EX" in postcode:
            if validate_postcode(postcode)[0]:
                valid = True
            else:
                print("Invalid postcode. Please enter in a valid format e.g. AB1 2CD or EG112EG")
        else:
            print("Invalid postcode. Please enter a postcode beginning with EX")

    valid = False

    while not valid:
        print("Enter a radius...")
        radius = input()
        if int(radius) in radius_inputs:
            valid = True
        else:
            print("Please enter a valid radius (1 , 2 , 5)")

    return postcode, radius
