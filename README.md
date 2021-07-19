# Encrypted-Personal-Password-Manager-GUI

</br>

# Desktop app to generate strong passwords and locally store your various login info to database in a secure format using symmetric encryption.

</br>

</br>

<img width="579" alt="mainapp" src="https://user-images.githubusercontent.com/74392848/126055460-9a4240f7-31f7-4f0d-a522-c06d9b483ecd.png">

</br>

Built with Python3 and Tkinter for the user interface. Sqlite3 is the database that stores your login credentials as organized seperate entries for each website or app you have to log into. We don't want to keep all of your user names and passwords stored in plain text though. Having your data stored using encryption adds a layer of security. This means that if someone was to directly access the database the information within it would be in an unreadable form. Only the 'Key' will be able to convert it back (decrypt) to it's original readable text format. This is what is referred to as symmetric encryption. The same key is used for both. Only the holder of this Key has the ability to encrypt and decrypt the contents stored in the data base. Encrypt them after they are entered and saved, then decrypt them before we request information from the database. We will use the Python library, Cryptography. In the cryptography library, there is a cryptography algorithm called fernet. We will use the fernet module to encrypt the file.
 

</br>

# Login Master Password Widget
</br>

<img width="545" alt="loginwidget" src="https://user-images.githubusercontent.com/74392848/126055443-83cac493-44c6-49a5-bfef-4999d884058d.png">

</br>

* #### When main.py is run, the Login widget will appear. You are required to enter your master password - this launches the main app.
* #### If it is your first time running this app, just enter what you wish to be your master password from now on and keep it somewhere safe.
* #### This password is required to use your encryption key that will be generated and stored for you.

# [Read Encryption Key Safety Information @ Bottom Of Page](#https://github.com/JaD33Z/Encrypted-Personal-Password-Manager-GUI/edit/master/README.md?plain=1#L81
)




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



* ## Show All Data In Database:

</br>

<img width="1103" alt="showalldata" src="https://user-images.githubusercontent.com/74392848/126055472-97f843b2-8b3f-4016-bb40-7d8dd7b2ed06.png">

</br>



* ## Remove Entry:

</br>

<img width="948" alt="remove" src="https://user-images.githubusercontent.com/74392848/126055987-867353c9-8c46-4fb7-94ca-4dd7b85fb89a.png">

</br>


# Safety with Encryption Key

</br>

### For transparency's sake, keep in mind this app is just a personal project for personal use for one user on their local machine. I would not recommend giving it a whirl in any corporate or shared setting with highly sensitive data or client/employee information. 

</br>

### That being said, let's give a deeper look into how the key - encryption relationship works, and why you must keep your key private - here is an example:

</br>

### The master password is stored encrypted, so if pw.txt was accessed your password would be unreadable and if you were to directly view the contents of your encrypted database file it would look something like this:

* ## *encrypted db view*
<img width="1255" alt="dbencrptd" src="https://user-images.githubusercontent.com/74392848/126056668-d5a74a0e-11f7-4bcf-abba-c748510c898c.png">

</br>

### *Not overly useful to someone trying to get your info... But, if they were to get your Key, they can decrypt your password and now have the authentication required to start the decryption process and get all of your data in plain text format.*

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

*and there is the ouptut of the formerly encrypted master password, '123'*


</br>

### Symmetric encryption does have drawbacks. Its weakest point is its aspects of key management. Because of this you can't promise that encrypted data is protected forever since the locally stored keys may get compromised. 

* ## In the case of this app, an extra step you could take to secure your data would be to move your "Key" to a seperate directory and store it there while you are not running the application:

<img width="631" alt="Screen Shot 2021-07-18 at 12 58 37 AM" src="https://user-images.githubusercontent.com/74392848/126056333-257ce15b-3f04-436e-b359-ae2667a17dc0.png">

* ###  **"Cut"** only the actual 'Key' text from the key.key file ( *Leave the blank "key.key" file where it is!* ) and **"Paste"** your Key to another file located in a seperate directory outside of the app. Then just copy and paste your 'Key' back into the key.key file before you run the app again.

* ###  Without the Key, the app cannot go past "Login", the main app cannot launch and the database contents stay irreversibly encrypted. (So don't lose your key!)

* ###  DO NOT move the *key.key*  **FILE**  itself to another directory, this could have very undesirable effects and get you locked out permanently if app is run without it.

* ### It's also a good idea to back up any important data.

</br>





</br>























