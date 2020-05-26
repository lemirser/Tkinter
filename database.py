from tkinter import *
from PIL import ImageTk, Image
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


def query():
    conn = sqlite3.connect("address_book.db")

    # Create cursor instance
    c = conn.cursor()

    # Query
    c.execute("SELECT oid, * FROM address;")
    results = c.fetchall()
    print(results)

    print_record = ""
    for result in results:
        print_record += f"Oid: {result[0]}\n\
        First Name: {result[1]}\n\
        Last Name: {result[2]}\n\
        Address: {result[3]}\n\
        City: {result[4]}\n\
        State: {result[5]}\n\
        Zipcode: {result[6]}\n\n"

    queryLabel = Label(root, text=print_record)
    queryLabel.grid(row=8, column=0, columnspan=2, sticky="W")

    # Commit chaches
    conn.commit()

    # Close connection
    conn.close()


# Create text box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, columnspan=2, padx=20)

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
f_nameLabel.grid(row=0, column=0, sticky="W")

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
queryButton = Button(root, text="Show button", command=query)
queryButton.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=86)

# Commit chaches
conn.commit()

# Close connection
conn.close()

root.mainloop()
