from cryptography.fernet import Fernet

class Cipher():

    def __init__(self):
        pass
        #masterkey = Fernet(key)

    # function to get sha 256 hash from key file
    def getHash(self):
        global key
        with open('./keys.key', 'rb') as f:
            content = f.readlines()
        content = [x.strip(b"\r\n") for x in content]
        key = content[1]
        masterKey = Fernet(key)

    # function to encrypt data
    def encrypt(self):
        pass

    #function to show key
    def showKey(self):
        print(key)
        print(len(key))
        print(type(key))
