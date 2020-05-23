from tkinter import *

# In Tkinter, everything is called widget.
# Root widget
root = Tk()

# Label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Gru")

# Possible call for myLabel/s
# myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)

# Position the labels by grid
# Rows and Columns starts at 0
# Rows and columns positions are relative
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# Event loop
root.mainloop()
