from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
root.minsize(600, 500)  # root.geometry("400x400")

var = StringVar()

c = Checkbutton(root, text="Checkbox 1", variable=var, onvalue="On", offvalue="Off")
c.deselect()  # Uncheck the checkbox by default
c.pack()


def show():
    myLabel = Label(root, text=var.get()).pack()


myButton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
