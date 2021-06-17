from cryptography.fernet import Fernet
import os.path

'''
# generate key
key = Fernet.generate_key()

# create file to store generated key
with open('filekey.key', 'wb') as f:
    f.write(key)
    f.close()
'''

print(os.path.exists("./encryption_test/encrypt_decrypt_test/pass.txt"))


# open filekey file to get generated key
with open('./encryption_test/encrypt_decrypt_test/filekey.key', 'rb') as f:
    key = f.read()

# create key using fernet and generated key
fernet = Fernet(key)

# opening the text file to encrypt the contents
with open('./encryption_test/encrypt_decrypt_test/pass.txt', 'rb') as f:
    original = f.read()

# encrypt file content
encrypted = fernet.encrypt(original)

# opening the text file and write encrypted data into text file
with open('./encryption_test/encrypt_decrypt_test/pass.txt', 'wb') as f:
    f.write(encrypted)
