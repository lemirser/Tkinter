from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
root.minsize(600, 500)


def open_file():
    """
    Will open a file directory based on `initaldir` and display it to the root window
    """
    global myImage
    root.filename = filedialog.askopenfilename(
        initialdir="images", title="Select a file!", filetypes=(("jpg files", "*.*"), ("all files", "*.*")),
    )

    myImage = ImageTk.PhotoImage(Image.open(root.filename).resize((680, 453), Image.ANTIALIAS))
    myLabel = Label(image=myImage).pack()


myButton = Button(root, text="Open file!", command=open_file).pack()

root.mainloop()
