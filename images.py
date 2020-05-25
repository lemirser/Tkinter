from tkinter import *
from PIL import ImageTk, Image
import os

cwd = os.getcwd()

# In Tkinter, everything is called widget.
# Root widget
root = Tk()
root.title("Tkinter App")

# Use .ico on root title bar
root.iconbitmap(f"{cwd}/icons/gor.ico")

# Use image
my_image = ImageTk.PhotoImage(Image.open(f"{cwd}/images/dog.jpg"))
my_label = Label(image=my_image)
my_label.pack()

button_quit = Button(root, text="Exit Program!", command=root.quit)
button_quit.pack()

root.mainloop()
