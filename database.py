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

# Create table
# c.execute(
#     """
#             CREATE TABLE address (
#                 first_name text,
#                 last_name text,
#                 address text,
#                 city text,
#                 state text,
#                 zipcode integer
#             )
#             """
# )


def is_submit():
    global f_name, l_name, address, city, state, zipcode

    conn = sqlite3.connect("address_book.db")

    # Create cursor instance
    c = conn.cursor()

    # Insert data
    c.execute(
        "INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            "f_name": f_name.get(),
            "l_name": l_name.get(),
            "address": address.get(),
            "city": city.get(),
            "state": state.get(),
            "zipcode": zipcode.get(),
        },
    )

    # Commit chaches
    conn.commit()

    # Close connection
    conn.close()

    f_name, l_name, address, city, state, zipcode = (
        f_name.delete(0, END),
        l_name.delete(0, END),
        address.delete(0, END),
        city.delete(0, END),
        state.delete(0, END),
        zipcode.delete(0, END),
    )


def get_users():
    conn = sqlite3.connect("address_book.db")

    # Create cursor instance
    c = conn.cursor()

    # Query
    c.execute("SELECT oid, * FROM address;")
    results = c.fetchall()
    print(results)

    print_record = ""
    for result in results:
        print_record += (
            f"Oid: {result[0]}\n"
            f"First Name: {result[1]}\n"
            f"Last Name: {result[2]}\n"
            f"Address: {result[3]}\n"
            f"State: {result[5]}\n"
            f"City: {result[4]}\n"
            f"Zipcode: {result[6]}\n\n"
        )

    # Commit chaches
    conn.commit()

    # Close connection
    conn.close()

    return print_record


def get_user():
    conn = sqlite3.connect("address_book.db")

    # Create cursor instance
    c = conn.cursor()

    # Query
    c.execute(
        "SELECT oid FROM address WHERE oid = :oid;", {"oid": searchbox_oid.get()},
    )
    result = c.fetchone()

    # Commit chaches
    conn.commit()

    # Close connection
    conn.close()

    if result:
        return True
    else:
        return False


def show_users():
    global queryLabel
    res = get_users()

    queryLabel.destroy()

    queryLabel = Label(root, text=res, justify=LEFT)
    queryLabel.grid(row=8, column=0, columnspan=2, sticky=W)


def clear_entry(event):
    "Event to clear the default text on searchbox_oid.entry"
    searchbox_oid.delete(0, END)


def delete_user():
    global searchbox_oid
    global deleteLabel
    deleteLabel.destroy()
    is_user = get_user()

    oid = searchbox_oid.get()

    deleteLabel = Label(root, text="", justify=CENTER)

    if is_user is False:
        deleteLabel.configure(text="No user found!")
    elif is_user is True:
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
            deleteLabel.configure(text="Successfully deleted user!")
        else:
            deleteLabel.configure(text="Cancelled process!")

    deleteLabel.grid(row=11, column=0, columnspan=3)


# Search entry widget
searchbox_oid = Entry(root, width=30)
searchbox_oid.grid(row=9, column=0, columnspan=2, padx=20, pady=(10, 0))

searchbox_oid.insert(0, "Enter OID")

# Bind the function to the event
# Ref: https://www.python-course.eu/tkinter_events_binds.php
searchbox_oid.bind("<FocusIn>", clear_entry)

deleteButton = Button(root, text="Delete user", command=delete_user)
deleteButton.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create text box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, columnspan=2, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, columnspan=2, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, columnspan=2, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, columnspan=2, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, columnspan=2, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, columnspan=2, padx=20)

# Create Textbox labels
f_nameLabel = Label(root, text="First name: ")
f_nameLabel.grid(row=0, column=0, sticky="W", pady=(10, 0))

l_nameLabel = Label(root, text="Last name: ")
l_nameLabel.grid(row=1, column=0, sticky="W")

addressLabel = Label(root, text="Address: ")
addressLabel.grid(row=2, column=0, sticky="W")

cityLabel = Label(root, text="City: ")
cityLabel.grid(row=3, column=0, sticky="W")

stateLabel = Label(root, text="State: ")
stateLabel.grid(row=4, column=0, sticky="W")

zipcodeLabel = Label(root, text="Zipcode: ")
zipcodeLabel.grid(row=5, column=0, sticky="W")

# Create submit button
submitButton = Button(root, text="Submit", command=is_submit)
submitButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
queryButton = Button(root, text="Show records", command=show_users)
queryButton.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=86)


queryLabel = Label(root, text="", justify=LEFT)
queryLabel.grid(row=8, column=0, columnspan=2, sticky=W)

deleteLabel = Label(root, text="")
deleteLabel.grid(row=11, column=1)

# Commit chaches
conn.commit()

# Close connection
conn.close()

root.mainloop()
