from tkinter import *
from PIL import ImageTk, Image

# In Tkinter, everything is called widget.
# Root widget
root = Tk()
root.title("Tkinter App")

# Use .ico on root title bar
root.iconbitmap("icons/gor.ico")

# Use image
my_img1 = ImageTk.PhotoImage(Image.open("images/dog.jpg").resize((680, 453), Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage(Image.open("images/pup1.jpg").resize((680, 453), Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage(Image.open("images/pup2.jpg").resize((680, 453), Image.ANTIALIAS))
my_img4 = ImageTk.PhotoImage(Image.open("images/pup3.jpg").resize((680, 453), Image.ANTIALIAS))

image_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(root, text=f"Image 1 of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)


def go_forward(img_index):
    """
    Display the next image

    Args:
        img_index {[int]} -- [index number]

    Returns:
        None
    """
    global my_label
    global button_forward
    global button_back

    # Removes the item currently displayed on the widget
    my_label.grid_forget()
    my_label = Label(image=image_list[img_index - 1])

    button_forward = Button(root, text=">>", command=lambda: go_forward(img_index + 1))
    button_back = Button(root, text="<<", command=lambda: go_back(img_index - 1))

    if img_index == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update status bar
    status = Label(root, text=f"Image {img_index} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def go_back(img_index):
    """
    Display the previous image

    Args:
        img_index {[int]} -- [index number]

    Returns:
        None
    """
    global my_label
    global button_forward
    global button_back

    # Removes the item currently displayed on the widget
    my_label.grid_forget()
    my_label = Label(image=image_list[img_index - 1])

    button_forward = Button(root, text=">>", command=lambda: go_forward(img_index + 1))
    button_back = Button(root, text="<<", command=lambda: go_back(img_index - 1))

    if img_index == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update status bar
    status = Label(root, text=f"Image {img_index} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", state=DISABLED, command=lambda: go_back(0))
button_forward = Button(root, text=">>", command=lambda: go_forward(2))
button_quit = Button(root, text="Exit Program!", command=root.quit)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
