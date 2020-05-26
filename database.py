from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
root.minsize(600, 500)  # root.geometry("400x400")

# SQLite Database
# Create a database or connect to one
# if db name doesn't exists, it will create it in the cwd
conn = sqlite3.connect("address_book.db")

# Create cursor instance
c = conn.cursor()

# Create table
c.execute(
    """
            CREATE TABLE address (
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer
            )
            """
)

# Commit chaches
conn.commit()

# Close connection
conn.close()

root.mainloop()
