import re
from tkinter import *


master = Tk()
master.geometry("500x500")
e = Entry(master)
e.place(x=215, y=225)
e1 = Entry(master)
e1.place(x=215, y=250)
e.focus_set()
e1.focus_set()

def callback():
    print (e.get())

b = Button(master, text="get", width=10, command=callback)
b.place(x=235, y=275)

mainloop()

e = Entry(master, width=50)
e1 = Entry(master, width=50)


postcode_text = e.get()
radius_text = e.get()

def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)

root = Tk()
my_gui = GUI(root)
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



