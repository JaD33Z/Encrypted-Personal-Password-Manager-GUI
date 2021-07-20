# Encrypted-Personal-Password-Manager-GUI

</br>

# Desktop app to generate strong passwords and locally store your various login info to database in a secure format using symmetric encryption.

</br>

</br>

<img width="579" alt="mainapp" src="https://user-images.githubusercontent.com/74392848/126055460-9a4240f7-31f7-4f0d-a522-c06d9b483ecd.png">

</br>

A secure vault for your collective login credentials with features including, a randomized password generator, a local database, that you will only have access to, where you can save, search, and delete the contents. Requiring the dual authentication of your master password and the generated "key". Your data will be safely kept using an encryption method which makes sure that the message encrypted cannot be manipulated/read without the key. It uses URL safe encoding for the keys. Fernet also uses 128-bit AES(Advanced Encryption Standard), in CBC(Cipher Block Chaining) mode and PKCS7 padding, with HMAC using SHA256 for authentication.

Having your data stored using encryption adds a layer of security. This means that if someone was to directly access the database the information within it would be in an unreadable form. User names and passwords should never be stored in plain text. 

Only the 'Key' will be able to convert your data back (decrypt) to it's original readable text format. This is what is referred to as symmetric encryption. The same key is used for both by both the sender and the receiver.  Only the holder of this Key has the ability to encrypt and decrypt the contents stored in the data base. Encrypts them after they are entered, then decrypts them before we request information from the database.

Built with Python3 and Tkinter library for the user interface. Sqlite3 is the database that stores your login credentials organized as seperate entries for each website or app that requires log info. We will use the Python library, Cryptography. In the cryptography library, there is a cryptography algorithm called fernet. We will use the fernet module to encrypt the file.
 

</br>

# Login Master Password Widget
</br>

<img width="545" alt="loginwidget" src="https://user-images.githubusercontent.com/74392848/126055443-83cac493-44c6-49a5-bfef-4999d884058d.png">

</br>

* #### When main.py is run, the Login widget will appear. You are required to enter your master password - Only after validation, the login widget will quit and this launches the main app window.
* #### If it is your first time running this app, just enter what you wish to be your master password from now on and keep it somewhere safe.
* #### This password is required to use your encryption key that will be generated and stored for you.

</br>

# *Read Encryption Key Safety Information @ Bottom Of Page!*





</br>

* ## Generate Strong Passwords:
</br>
<img width="586" alt="Screen Shot 2021-07-18 at 12 31 44 AM" src="https://user-images.githubusercontent.com/74392848/126055995-ac46e48e-afa2-4158-8796-7e5ab05fd7b6.png">

</br>

* ## Save Login Information:

</br>

<img width="915" alt="save2" src="https://user-images.githubusercontent.com/74392848/126055426-806be6ea-3201-468c-a948-70591712f85c.png">

</br>

* ## Search For Login Credentials By Name Of Site:

</br>

<img width="891" alt="searchname" src="https://user-images.githubusercontent.com/74392848/126055501-5e056eb4-c8df-4fab-9119-5c7c0a39a27d.png">

</br>

#### Displays the credentials from your search result in a messagebox window, also prints them to the terminal.

</br>



* ## Show All Data In Database:

</br>

<img width="1103" alt="showalldata" src="https://user-images.githubusercontent.com/74392848/126055472-97f843b2-8b3f-4016-bb40-7d8dd7b2ed06.png">

</br>

#### Prints all of your contents in their original decrypted format to your terminal window. 

</br>



* ## Remove Entry:

</br>

<img width="948" alt="remove" src="https://user-images.githubusercontent.com/74392848/126055987-867353c9-8c46-4fb7-94ca-4dd7b85fb89a.png">

</br>


# Important! - Safety with Encryption Key:

</br>

#### For transparency's sake, keep in mind this app is just a personal project for personal use, meant for a single user on their local machine. I would not recommend giving it a whirl in any corporate or shared settings with highly sensitive data or client/employee information. 


#### That being said, let's have a deeper look into how the key - encryption relationship works, and why you must keep your key private - here is an example:


#### The master password is stored encrypted, so if pw.txt was accessed your password would be unreadable and if you were to directly view the contents of your encrypted database file it would look something like this:

* ## *encrypted db view*
<img width="1255" alt="dbencrptd" src="https://user-images.githubusercontent.com/74392848/126056668-d5a74a0e-11f7-4bcf-abba-c748510c898c.png">

### *Not overly useful to someone trying to get your info...* 
## But, if they were to get your Key, they can decrypt your password and now have the authentication required to start the decryption process and get all of your data in plain text format.

* See code below:

```python

# string from key.key 
key_str = 'bWyo52t1dSnwi-KpvLM2OhUsn-i1jeV-MLuPj9Ud2cw='
key = str.encode(key_str)

# actual encrypted version of master password(123) from pw.txt
password_str = 'gAAAAABg77PHASqKZlKkQOuNersMJEBl3JVpBhJebbI0emQK_lbU9HOfQnPi2vIAcVmczyapwsJk_HrlDd514_2Xz6qMmHKiPQ=='
password = str.encode(password_str)

f = Fernet(key)

plain_text = f.decrypt(password)
print(plain_text)

# output:
#          b'123'

```

#### *and there is the ouptut containing our formerly encrypted master password, '123'*


</br>

### Symmetric encryption does have drawbacks. Its weakest point is its aspects of key management. Because of this you can't promise that encrypted data is protected forever since the locally stored keys may get compromised. 

* ## In the case of this app, an extra step you could take to secure your data would be to move your "Key" to a separate directory and store it there while you are not running the application:

<img width="631" alt="Screen Shot 2021-07-18 at 12 58 37 AM" src="https://user-images.githubusercontent.com/74392848/126056333-257ce15b-3f04-436e-b359-ae2667a17dc0.png">

* ###  **"Cut"** ONLY the actual 'Key' text from the key.key file ( *Leave the blank "key.key" file where it is!* )

* ### **"Paste"** your Key to another file located in a separate directory outside of the app. Then just copy and paste your 'Key' back into the 'key.key' file before you run the app again.

* ###  Without the Key in the 'key.key' file, the app cannot go past "Login", the main app cannot launch and the database contents stay irreversibly encrypted. (So don't lose your key!)

* ###  DO NOT move the actual *key.key*  **FILE**  itself to another directory, this could have very undesirable effects and get you locked out permanently if app is run without it.

* ### It's also a good idea to back up any important data.

</br>





</br>























