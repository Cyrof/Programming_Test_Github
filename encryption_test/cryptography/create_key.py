import hashlib
import base64
import os
from typing import Text
from cryptography import fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

'''
# generate sha256 hash of master pass and store in file
key = 'doraemon'
encrypt = hashlib.sha256(key.encode()).hexdigest()

# open file and write key into file
with open('./encryption_test/cryptography/text.txt', 'w+') as f:
    f.write(encrypt)
    f.close
'''


# function to create master key
def pass_key(master_pass):
    global master_key
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                     salt=salt, iterations=100000,)

    key = base64.urlsafe_b64encode(kdf.derive(master_pass.encode('utf-8')))
    master_key = Fernet(key)

# prompt user for new text, encrypt and store in file


def new_text():
    text = input("Enter text: ")
    text = master_key.encrypt(text.encode('utf-8'))
    with open('./encryption_test/cryptography/text.txt', 'ab') as f:
        f.write(b"\n" + text)
        f.close()

# decrypt and show user content of file


def view():
    with open('./encryption_test/cryptography/text.txt', 'rb+') as f:
        content = f.read()[65:]
        #decrypted = master_key.decrypt(content)
        print(type(content))


# choice function
def choice(opt):
    if opt == 1:
        new_text()
    elif opt == 2:
        view()

# menu function


def menu():
    while True:
        print("\nEnter text\t[1]")
        print("View All\t[2]")
        print("Quit\t\t[3]")
        option = int(input("Enter your choice: "))
        if option != 3:
            choice(option)
        else:
            break


# function to check if user inputted master pass is correct
def checker(master_pass):
    encrypted_pass = hashlib.sha256(master_pass.encode()).hexdigest()

    with open('./encryption_test/cryptography/text.txt', 'r+') as f:
        line = f.readlines()
        print(line)
        print(encrypted_pass)

    if encrypted_pass == line[0].replace('\n', ''):
        key = pass_key(master_pass)
        menu()
    else:
        print("Wrong master password!")


# user input to prompt user for master pass
def user():
    master_pass = input("Enter master password: ")
    checker(master_pass)


if __name__ == "__main__":
    user()
