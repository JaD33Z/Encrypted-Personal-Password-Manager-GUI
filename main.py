from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import sqlite3
from entry import Login



conn = sqlite3.connect('pw.db')
c = conn.cursor()



# ---------------------------- PASSWORD GENERATOR -------------------------------------------- #


# Generate Password button function. Returns randomized very strong passwords.


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)



# ---------------------------- SAVE ENTRY: WEBSITE, USERNAME, PASSWORD ----------------------- #


# Add button function, fill out all fields and your entry will be saved to the database.


def save_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="To Add an entry to the database, Please make sure you haven't"
                                    " left any fields empty.\n\nGenerate a secure password or make your own."
                                    "\n\nFetch credentials with website name and search button.")

    else:
        try:
            login_window.decrypt_db()

        except TypeError:
            pass

        finally:

            with conn:
                c.execute("INSERT INTO passwords VALUES (:website, :email, :password)",
                          {'website': website, 'email': email, 'password': password})
                messagebox.showinfo(title="Saved", message=f"{website} entry saved.")

            login_window.encrypt_db()
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            print("data saved Successfully")



# ---------------------------- FIND PASSWORD ------------------------------------------------ #


# Search button function. Enter website name in field and returns details for requested entry.


def find_password():
    website = website_entry.get()
    login_window.decrypt_db()
    c.execute("SELECT * FROM passwords WHERE website=:website", {'website': website})
    rows = c.fetchall()

    if len(website) == 0 or len(rows) == 0:
        messagebox.showinfo(title="Error", message="No details for that site exist.")
        login_window.encrypt_db()

    else:
        for row in rows:
            print(row)
            email = row[1]
            password = row[2]
            messagebox.showinfo(title=website, message=f"Username: {email}\nPassword: {password}")
        login_window.encrypt_db()



# ----------------------------- DELETE ENTRY ----------------------------------------------- #


# Remove button function. Enter name in the website field and it removes the entry from data base.


def delete_entry():
    remove_row = website_entry.get()
    login_window.decrypt_db()

    if remove_row:
        c.execute("DELETE FROM passwords WHERE website=?", (remove_row,))
        conn.commit()
        messagebox.showinfo(title="Okay", message=f"Details for {remove_row} removed from database.")
        website_entry.delete(0, END)

    else:
        messagebox.showinfo(title="Error", message="No details for that site exist.")

    login_window.encrypt_db()



# ----------------------------- SHOW ALL ENTRIES -------------------------------------------- #


## Show All button function. Prints out all your database contents, view them in terminal.


def show_all():
    login_window.decrypt_db()
    c.execute("SELECT * FROM passwords")
    rows = c.fetchall()
    for row in rows:
        print(row)

    login_window.encrypt_db()



# ---------------------------- MAIN UI SETUP --------------------------------------------------- #


# Main Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='gray10')

# Transitions from Login widget to Main app gui after validation
window.withdraw()
login_window = Login(window)


# Canvas/Image
canvas = Canvas(height=200, width=200, bg='gray10')
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=20)


# Labels
website_label = Label(text="Website:", bg='gray10', fg='white')
website_label.grid(row=1, column=0)

email_label = Label(text="Username:", bg='gray10', fg='white')
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg='gray10', fg='white')
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=28, bg='pale green', borderwidth=4, relief=SUNKEN)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=28, bg='pale green', borderwidth=4, relief=SUNKEN)
email_entry.grid(row=2, column=1, columnspan=1)

email_entry.insert(0, "youremail@gmail.com")
password_entry = Entry(width=28, bg='pale green', borderwidth=4, relief=SUNKEN)
password_entry.grid(row=3, column=1)


# Buttons
search_button = Button(text="Search", width=14, command=find_password, fg='black', highlightbackground='black')
search_button.grid(row=1, column=2, padx=5, pady=10)

generate_password_button = Button(text="Generate Password", command=generate_password, fg='black', highlightbackground='black')
generate_password_button.grid(row=3, column=2, padx=5, pady=10)

add_button = Button(text="Add", width=14, command=save_entry, fg='black', highlightbackground='black')
add_button.grid(row=2, column=2, padx=5, pady=10)

remove_button = Button(text="Remove", width=14, command=delete_entry, fg='black', highlightbackground='black')
remove_button.grid(row=4, column=1, padx=5, pady=30)

show_button = Button(text="Show all", width=14, command=show_all, fg='black', highlightbackground='black')
show_button.grid(row=4, column=2, padx=5, pady=30)


window.mainloop()

