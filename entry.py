from cryptography.fernet import Fernet
from tkinter import *
import sqlite3
import os
import os.path
from tkinter import messagebox



conn = sqlite3.connect('pw.db')
c = conn.cursor()


# ------------------------------ LOGIN UI AND VALIDATION  ------------------------------------ #


#  The Login class handles all validation and encryption for the app.


class Login(Toplevel):
    def __init__(self, root):
        super().__init__(root)

        self.root = root

        self.password_label = Label(self, text="Password:")
        self.password_entry = Entry(self, bg='pale green', borderwidth=4, relief=SUNKEN)
        self.submit = Button(self, text="Login", command=self.validate_login)

        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.submit.grid(row=2, column=1)



    def generate_key(self):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.seek(0)
            key_file.write(key)



    def load_key(self):
        return open('key.key', 'rb').read()



    def encrypt_db(self):
        with open('pw.db', 'rb') as to_encrypt:
            key = self.load_key()
            f_key = Fernet(key)
            message = to_encrypt.read()
            encrypted_message = f_key.encrypt(message)
            with open('pw.db', 'wb') as encrypt_entry:
                encrypt_entry.write(encrypted_message)



    def decrypt_db(self):
        with open('pw.db', 'rb') as to_decrypt:
            key = self.load_key()
            f_key = Fernet(key)
            message = to_decrypt.read()
            decrypted_data = f_key.decrypt(message)
            with open('pw.db', 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)



    def decrypt_password(self):
        key = self.load_key()
        with open('pw.txt', 'rb') as file:
            read_pw = file.read()
            f_key = Fernet(key)
            plain_password = f_key.decrypt(read_pw)
            plain_password = plain_password.decode()
            return plain_password



    # Validates log in entry, if master password matches - launch main gui.
    # On first run, type whatever you wish to be your master password in the login widget.
    # Creates new key, password file, and database if one does not already exist.


    def validate_login(self):
        if not os.path.isfile('key.key'):
            self.generate_key()
            key = self.load_key()
            f_key = Fernet(key)

            with open('pw.txt', 'wb') as pw_file:
                pw_file.seek(0)
                master_password = self.password_entry.get()
                plaintext_password = master_password.encode()
                encrypted_password = f_key.encrypt(plaintext_password)
                pw_file.write(encrypted_password)

            c.execute("""CREATE TABLE passwords (
                                website text,
                                email text,
                                password text
                                )""")
            print("Database connection is established successfully!")
            self.withdraw()
            self.root.deiconify()

        else:
            with open('pw.txt', 'rb') as pw_file:
                attempt_login = self.password_entry.get()
                plaintext_password = self.decrypt_password()
                if attempt_login == plaintext_password:
                    print("Welcome Back!")
                    self.withdraw()
                    self.root.deiconify()
                else:
                    messagebox.showinfo(title="Log In",
                                        message="Password Incorrect! Log in attempt failed.")

