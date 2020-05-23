from tkinter import *

# In Tkinter, everything is called widget.
# Root widget
root = Tk()

# Label widget
myLabel = Label(root, text="Hello World!")

# Packing the label into the root widget
myLabel.pack()

# Event loop
root.mainloop()
