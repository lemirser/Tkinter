from tkinter import *

# In Tkinter, everything is called widget.
# Root widget
root = Tk()


def myClick():
    myLabel = Label(root, text="Clicked")
    myLabel.pack()


"""
Button widget, (where to place the button, display name)
    state = Disables or enables the button
    padx & pady = increase the padding of the button
    fg = textcolor
    bg = background color
"""
myButton = Button(root, text="Click Me!", padx=50, pady=10, command=myClick, fg="red", bg="blue")
myButton.pack()

# Event loop
root.mainloop()
