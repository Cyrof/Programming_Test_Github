import hashlib
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# class to create master ps, ps hash and sha 256 hash for cipher
class Masterpass():

    # default constructor
    def __init__(self):
        pass

    # function to create sha 256 hash
    def createKey(self, password):
        hashCheck = hashlib.sha256(password.encode()).hexdigest()

        with open('./keys.key', 'w+') as f:
            f.write(hashCheck + "\n")
            f.close()
        print("\nSaving hash")
        
    # create key for ciphering
    def keyForEncryption(self, password):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                         salt=salt, iterations=100000,)

        key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
        
        with open('./keys.key', 'ab+') as f:
            f.write(key)
        print("Saving master key")

    # prompt user to enter ps
    def createMaster(self):
        password = input("Enter password: ")
        password_check = input("Confirm password: ")

        if password == password_check:
            self.createKey(password=password)
            self.keyForEncryption(password=password)
        else:
            print("Password do not match!")
            self.createMaster()

    # prompt user to create ps
    def user(self):
        userchoice = input("Would you like to create a masterpassword? [y/n]: ")

        if userchoice.lower() == "y":
            self.createMaster()
        else:
            secondPrompt = input("Are you sure you want to exit? [y/n]: ")

            if secondPrompt.lower() == "n":
                self.user()
            else:
                pass

    # check if key file is empty 
    def checkFile(self):
        check = os.stat('./keys.key').st_size
        return check

    # delete content in key file
    def reset(self):
        with open('./keys.key', 'w') as f:
            f.write("")
            f.close() 
    
    # check if inputted master ps is correct 
    def checker(self, password):
        with open('./keys.key', 'r+') as f:
            content = f.readlines()
        content = [x.strip("\n") for x in content]

        if password == content[0]:
            return True
        else:
            return False
        



