from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
root.minsize(600, 500)  # root.geometry("400x400")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
# Way 1
# clicked.set("Monday")
# Way 2
clicked.set(days[0])

# clicked is a variable
# Way 1
# drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Way 2
drop = OptionMenu(root, clicked, *days)
drop.pack()


def is_clicked():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()


myButton = Button(root, text="Click me!", command=is_clicked)
myButton.pack()

root.mainloop()
