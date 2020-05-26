from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
root.minsize(600, 500)  # root.geometry("400x400")

# Scall widget or vertical slider
# It is important to pack the Scale into its onw line
vertical = Scale(root, from_=0, to=500)
vertical.pack()

myl = Label(root, text="%").pack()
horizontal = Scale(root, from_=0, to=10, orient=HORIZONTAL)
horizontal.pack()


def slide():
    if horizontal.get() > 4:
        my_label = Label(root, text="Greater than 4.").pack()
    else:
        my_label = Label(root, text="Less than 4").pack()


my_btn = Button(root, text="Click me!", command=slide).pack()

root.mainloop()
