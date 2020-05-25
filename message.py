from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# In Tkinter, everything is called widget.
# Root widget
root = Tk()
root.title("Tkinter App")

# Use .ico on root title bar
root.iconbitmap("icons/gor.ico")

# Setting minimum window size for root widget
root.minsize(600, 500)

"""
Messagebox methods:
    showinfo(TITLE, MESSAGE)
    showwarning(TITLE, MESSAGE)
    showerror(TITLE, MESSAGE)
    askquestion(TITLE, MESSAGE)
    askokcancel(TITLE, MESSAGE)
    askyesno(TITLE, MESSAGE)
"""


def popup():
    """
    This will display a messsage box and returns/displays "Yes" / "No" on the Label widget.

    Args:
        None

    Returns:
        Yes / No {[String]}
    """
    response = messagebox.askyesno("This is my Popup!", "Hello World!")

    if response:
        Label(root, text="Yes").pack()
    else:
        Label(root, text="No").pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()
