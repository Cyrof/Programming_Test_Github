# this is a password vault system 
# to use, it requires a master password to access the other 
# passwords and usernames stored in the vault 

# import lib
import base64
import os
from cryptography import fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# initialise variable
userlist = [] # initialise user list to store username and password for encryption

# using master password to create key 
# the master password
# function to create master key using master password
def masterkey(key):
    password = b"doraemon"

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000,)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)

# function to encrypt text 
def encrypt():
    pass

# function to decrypt text
def decrypt():
    pass

# function to read file
def file():
    content = []
    with open('./password_safe/vault.csv', 'rb+') as f:
        
        next(f)
        for line in f:
            l = line.decode('ascii').replace('\r\n', '')
            content.append(l)
    return content

# function to get user to input username and password
def user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    userlist.append(username)
    userlist.append(password)

    
# choice function
def choice(opt):
    if opt == 1:
        user()
    elif opt == 2:
        pass

# menu function to continue prompting user till user select quit
def menu():
    for x in range(3):
        masterpass = input("Enter the masterpassword to access vault: ")

    while True:
        print("\nEnter new password and username\t[1]")
        print("View all password and username\t[2]")
        print("Quit\t\t\t\t[3]")
        option = int(input("Enter your choice: "))
        if option != 3:
            choice(option)
        else:
            break 
    

if __name__ == "__main__":
    content = file()
    print(content)