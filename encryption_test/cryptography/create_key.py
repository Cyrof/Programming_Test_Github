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
    print(key)


# functions to encrypt and decrypt
def encrypt(text):
    encrypted = master_key.encrypt(text)

    with open('./encryption_test/cryptography/text.txt', 'ab+') as f:
        f.write(encrypted + b"\n")
        f.close()


def decrypt():
    with open('./encryption_test/cryptography/text.txt', 'rb+') as f:
        content = f.read()
    decrypted = master_key.decrypt(content)
    print(decrypted)
    


# function to prompt user to enter text
def text():
    user_text = input("Enter text: ").encode()
    print("Saving to file.")
    encrypt(user_text)
    # write(user_text)


# choice function
def choice(opt):
    if opt == 1:
        text()
    elif opt == 2:
        decrypt()

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

    try:
        with open('./encryption_test/cryptography/masterpass.txt', 'r+') as f:
            line = f.readlines()

        if encrypted_pass == line[0].replace('\n', ''):
            key = pass_key(master_pass)
            menu()
        else:
            print("Wrong master password!")
    except IndexError:
        print("Nothing in file")


# user input to prompt user for master pass
def user():
    master_pass = input("Enter master password: ")
    checker(master_pass)


if __name__ == "__main__":
    user()
