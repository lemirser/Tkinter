from tkinter import *
from PIL import ImageTk, Image

# In Tkinter, everything is called widget.
# Root widget
root = Tk()
root.title("Tkinter App")

# Use .ico on root title bar
root.iconbitmap("icons/gor.ico")

# Setting minimum window size for root widget
root.minsize(600, 500)

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

# Radio button variable
pizza = StringVar()

# Radio button default option
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode, command=lambda: is_clicked(pizza.get())).pack(anchor=W)


def is_clicked(value):
    myLabel = Label(root, text=value).pack()


# Creating radio button
# Radiobutton(root, text="Int 1", variable=r1, value=1, command=lambda: is_clicked(r1.get())).pack()
# Radiobutton(root, text="Int 2", variable=r1, value=2, command=lambda: is_clicked(r1.get())).pack()

# myLabel = Label(root, text=pizza.get()).pack()

myButton = Button(root, text="Click me!", command=lambda: is_clicked(pizza.get())).pack()

root.mainloop()
