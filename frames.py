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

frame = LabelFrame(root, text="This is a frame", padx=20, pady=20)
frame.pack(padx=10, pady=10)

# We can use grid and pack at the same time with LabelFrame widget
b1 = Button(frame, text="Button 1")
b2 = Button(frame, text="Button 2")
b3 = Button(frame, text="Button 3")
b1.grid(row=0, column=0, padx=5, pady=5)
b2.grid(row=0, column=1, padx=5, pady=5)
b3.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
