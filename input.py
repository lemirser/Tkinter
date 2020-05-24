from tkinter import *

# In Tkinter, everything is called widget.
# Root widget
root = Tk()

# Entry widget is equivalent to input
e = Entry(root, width=50, borderwidth=5)

# Will add a default text on the entry widget
e.insert(0, "Enter your name: ")


def clear_entry(event):
    "Event to clear the default text on e.entry"
    e.delete(0, END)


# Bind the function to the event
# Ref: https://www.python-course.eu/tkinter_events_binds.php
e.bind("<FocusIn>", clear_entry)

e.pack()

e1 = Entry(root)
e1.insert(0, "Test")
e1.pack()


def myClick():
    myLabel = Label(root, text="Clicked")
    myLabel.pack()


def getName():
    "This will return what your entry on e.Entry widget as a label widget"
    message = f"Hello {e.get().title()}!"
    myName = Label(root, text=message)
    myName.pack()


"""
Button widget, (where to place the button, display name)
    state = Disables or enables the button
    padx & pady = increase the padding of the button
    fg = textcolor
    bg = background color
    command = for functions
"""
myButton = Button(root, text="Enter Your name!", padx=50, pady=10, command=getName, fg="red", bg="blue")
myButton.pack()

# Event loop
root.mainloop()
