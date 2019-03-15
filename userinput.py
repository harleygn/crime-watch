import re
from tkinter import *


master = Tk()
master.geometry("250x500")
e = Entry(master)
e.place(x=65, y=225)
e.focus_set()

def callback():
    print (e.get())

b = Button(master, text="Start", width=10, command=callback)
b.place(x=85, y=375)

variable = StringVar(master)
variable.set("Radius") # default value

w = OptionMenu(master, variable, "1", "2", "5")
w.place(x=85, y=275)

mainloop()

e = Entry(master, width=50)

postcode_text = e.get()
radius_text = e.get()

content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)

root = Tk()
root.mainloop()

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
            print("Please enter a radius between 0 and 5.")

    return postcode, radius



