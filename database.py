from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
root.minsize(300, 250)  # root.geometry("400x400")

# SQLite Database
# Create a database or connect to one
# if db name doesn't exists, it will create it in the cwd
conn = sqlite3.connect("address_book.db")

# Create cursor instance
c = conn.cursor()


def is_submit():
    """
    Function to insert user details in the database.
    """

    global f_name, l_name, address, city, state, zipcode

    fname = f_name.get()
    lname = l_name.get()
    add = address.get()
    cit = city.get()
    stat = state.get()
    zipc = zipcode.get()

    conn = sqlite3.connect("address_book.db")

    # Create cursor instance
    c = conn.cursor()

    # Insert data
    c.execute(
        "INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {"f_name": fname, "l_name": lname, "address": add, "city": cit, "state": stat, "zipcode": zipc,},
    )

    # Commit chaches
    conn.commit()

    # Close connection
    conn.close()


def get_user():
    """
    Fetch a user if it's existing in the database and return the user oid for deletion reference.

    Returns:
        True / False {(bool)}
            -- if the user is in the data base return True else False.
    """
    conn = sqlite3.connect("address_book.db")

    # Create cursor instance
    c = conn.cursor()

    if searchbox_oid.get():
        # Query
        c.execute(
            "SELECT oid, * FROM address WHERE oid = :oid;", {"oid": searchbox_oid.get()},
        )
    else:
        c.execute("SELECT oid, * FROM address;")
    result = c.fetchall()

    print_record = ""
    for item in result:
        print_record += (
            f"Oid: {item[0]}\n"
            f"First Name: {item[1]}\n"
            f"Last Name: {item[2]}\n"
            f"Address: {item[3]}\n"
            f"State: {item[5]}\n"
            f"City: {item[4]}\n"
            f"Zipcode: {item[6]}\n\n"
        )

    # Commit chaches
    conn.commit()

    # Close connection
    conn.close()

    if result:
        return print_record


def show_users():
    """
    Display all the users and their info in the label widget.
    """
    global queryLabel
    res = get_user()

    print(res)

    queryLabel.destroy()

    queryLabel = Label(root, text=res, justify=LEFT)
    queryLabel.grid(row=12, column=0, columnspan=2, sticky=W)


def delete_user():
    """
    Delete a user if it's in the database
    """
    global searchbox_oid
    global queryLabel
    queryLabel.destroy()
    is_user = get_user()

    oid = searchbox_oid.get()

    queryLabel = Label(root, text="", justify=CENTER)

    if oid:
        if is_user:
            response = messagebox.askyesno("Delete user!", "Are you sure you want to permanently delete this user?")
            if response:

                conn = sqlite3.connect("address_book.db")

                # Create cursor instance
                c = conn.cursor()

                # Query
                c.execute(
                    "DELETE FROM address WHERE OID = :oid;", {"oid": oid},
                )

                # Commit chaches
                conn.commit()

                # Close connection
                conn.close()
                queryLabel.configure(text="Successfully deleted user!")

            else:
                queryLabel.configure(text="Cancelled process!")
        elif is_user is None:
            queryLabel.configure(text="No user found!")
    else:
        queryLabel.configure(text="User OID is required!")
    queryLabel.grid(row=12, column=0, columnspan=2)


def edit_user():
    editor = Tk()
    editor.title("Tkinter App/ Edit user")
    editor.iconbitmap("icons/gor.ico")
    editor.minsize(300, 250)  # root.geometry("400x400")

    global f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zipcode_editor

    # Button widgets
    submitButton_editor = Button(editor, text="Save")

    # Entry widgets
    f_name_editor = Entry(editor, width=30)
    l_name_editor = Entry(editor, width=30)
    address_editor = Entry(editor, width=30)
    city_editor = Entry(editor, width=30)
    state_editor = Entry(editor, width=30)
    zipcode_editor = Entry(editor, width=30)

    # Label widgets
    f_nameLabel_editor = Label(editor, text="First name: ")
    l_nameLabel_editor = Label(editor, text="Last name: ")
    addressLabel_editor = Label(editor, text="Address: ")
    cityLabel_editor = Label(editor, text="City: ")
    stateLabel_editor = Label(editor, text="State: ")
    zipcodeLabel_editor = Label(editor, text="Zipcode: ")

    # Grids
    f_nameLabel_editor.grid(row=0, column=0, sticky="W", pady=(10, 0))
    l_nameLabel_editor.grid(row=1, column=0, sticky="W")
    addressLabel_editor.grid(row=2, column=0, sticky="W")
    cityLabel_editor.grid(row=3, column=0, sticky="W")
    stateLabel_editor.grid(row=4, column=0, sticky="W")
    zipcodeLabel_editor.grid(row=5, column=0, sticky="W")

    f_name_editor.grid(row=0, column=1, columnspan=2, padx=20, pady=(10, 0))
    l_name_editor.grid(row=1, column=1, columnspan=2, padx=20)
    address_editor.grid(row=2, column=1, columnspan=2, padx=20)
    city_editor.grid(row=3, column=1, columnspan=2, padx=20)
    state_editor.grid(row=4, column=1, columnspan=2, padx=20)
    zipcode_editor.grid(row=5, column=1, columnspan=2, padx=20)

    conn = sqlite3.connect("address_book.db")

    # Create cursor instance
    c = conn.cursor()

    c.execute(
        "SELECT * FROM address WHERE oid = :oid;", {"oid": searchbox_oid.get()},
    )
    result = c.fetchone()

    # Commit chaches
    conn.commit()

    # Close connection
    conn.close()

    f_name_editor.insert(0, result[0])
    l_name_editor.insert(0, result[1])
    address_editor.insert(0, result[2])
    city_editor.insert(0, result[3])
    state_editor.insert(0, result[4])
    zipcode_editor.insert(0, result[5])
    # Grid
    submitButton_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)


def clear_entry(event):
    "Event to clear the default text on searchbox_oid.entry"
    searchbox_oid.delete(0, END)


# Button widgets
submitButton = Button(root, text="Submit", command=is_submit)

queryButton = Button(root, text="Show records", command=show_users)

deleteButton = Button(root, text="Delete user", command=delete_user)

updateButton = Button(root, text="Update user", command=edit_user)


# Entry widgets
f_name = Entry(root, width=30)
l_name = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
state = Entry(root, width=30)
zipcode = Entry(root, width=30)

searchbox_oid = Entry(root, width=30)


# Label widgets
f_nameLabel = Label(root, text="First name: ")
l_nameLabel = Label(root, text="Last name: ")
addressLabel = Label(root, text="Address: ")
cityLabel = Label(root, text="City: ")
stateLabel = Label(root, text="State: ")
zipcodeLabel = Label(root, text="Zipcode: ")

queryLabel = Label(root, text="", justify=LEFT)

deleteLabel = Label(root, text="")

searchoidLabel = Label(root, text="Enter user OID:")


# Grids
f_nameLabel.grid(row=0, column=0, sticky="W", pady=(10, 0))
l_nameLabel.grid(row=1, column=0, sticky="W")
addressLabel.grid(row=2, column=0, sticky="W")
cityLabel.grid(row=3, column=0, sticky="W")
stateLabel.grid(row=4, column=0, sticky="W")
zipcodeLabel.grid(row=5, column=0, sticky="W")

f_name.grid(row=0, column=1, columnspan=2, padx=20, pady=(10, 0))
l_name.grid(row=1, column=1, columnspan=2, padx=20)
address.grid(row=2, column=1, columnspan=2, padx=20)
city.grid(row=3, column=1, columnspan=2, padx=20)
state.grid(row=4, column=1, columnspan=2, padx=20)
zipcode.grid(row=5, column=1, columnspan=2, padx=20)

submitButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

queryButton.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=93)

searchbox_oid.grid(row=8, column=1, columnspan=2, padx=20, pady=(10, 0))

searchoidLabel.grid(row=8, column=0, pady=(10, 0))

deleteButton.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

updateButton.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=96)

deleteLabel.grid(row=11, column=1)

queryLabel.grid(row=12, column=0, columnspan=2, sticky=W)


# Bind the function to the event
# Ref: https://www.python-course.eu/tkinter_events_binds.php
searchbox_oid.bind("<FocusIn>", clear_entry)


# Commit chaches
conn.commit()

# Close connection
conn.close()

root.mainloop()
