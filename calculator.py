from tkinter import *

# In Tkinter, everything is called widget.
# Root widget
root = Tk()
root.title("Simple Calculator")

# Entry widget is equivalent to input
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    """
    Returns number based on the button you clicked

    Args:
        number: int

    Returns:
        String
    """
    current = str(e.get())
    e.delete(0, END)
    e.insert(0, current + str(number))


def clear_entry():
    "Delete numbers in the entry widget"
    e.delete(0, END)


def add_num():
    """
    Fetch the first entry on entry widget and save it to fist_number variable then create global variable
    in order to use the first_number value to a different function.

    Args:
        None

    Returns:
        None
    """
    first_number = e.get()
    global f_num, op
    op = "+"
    f_num = int(first_number)
    e.delete(0, END)


def subtract_num():
    """
    Subtract values

    Args:
        None

    Returns:
        None
    """
    first_number = e.get()
    global f_num, op
    f_num = int(first_number)
    op = "-"
    e.delete(0, END)


def multiply_num():
    """
    Multiply values

    Args:
        None

    Returns:
        None
    """
    first_number = e.get()
    global f_num, op
    f_num = int(first_number)
    op = "*"
    e.delete(0, END)


def divide_num():
    """
    Divides values

    Args:
        None

    Returns:
        None
    """
    first_number = e.get()
    global f_num, op
    f_num = int(first_number)
    op = "/"
    e.delete(0, END)


def get_total():
    """
    Add the two numbers

    Args:
        None

    Returns:
        Int
    """
    second_number = e.get()
    e.delete(0, END)

    if op == "+":
        e.insert(0, f_num + int(second_number))
    elif op == "-":
        e.insert(0, f_num - int(second_number))
    elif op == "*":
        e.insert(0, f_num * int(second_number))
    elif op == "/":
        e.insert(0, f_num / int(second_number))


# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39.5, pady=20, command=add_num)
button_mul = Button(root, text="*", padx=40, pady=20, command=multiply_num)
button_sub = Button(root, text="-", padx=40, pady=20, command=subtract_num)
button_div = Button(root, text="/", padx=40, pady=20, command=divide_num)
button_total = Button(root, text="=", padx=39, pady=20, command=get_total)
button_clear = Button(root, text="Clear", padx=30, pady=20, command=lambda: clear_entry())

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)


button_0.grid(row=4, column=0)
button_total.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_div.grid(row=4, column=3)

# button_add.grid(row=5, column=0)

# Event loop

root.mainloop()
