from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
root.minsize(600, 500)


def open_window():
    global my_image
    top = Toplevel()
    top.title("Tkinter App/ Top Level")
    top.iconbitmap("icons/gor.ico")
    my_image = ImageTk.PhotoImage(Image.open("images/dog.jpg"))
    label1 = Label(top, image=my_image).pack()
    label2 = Label(top, text="Dawg").pack()


btn = Button(root, text="Open 2nd window", command=open_window).pack()

root.mainloop()
