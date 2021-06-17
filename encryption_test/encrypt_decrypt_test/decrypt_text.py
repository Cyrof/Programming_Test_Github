from cryptography.fernet import Fernet

# open file to get generated key 
with open('./encryption_test/encrypt_decrypt_test/filekey.key', 'rb') as f:
    key = f.read()

# create key using fernet and generated key 
fernet = Fernet(key)

# open the text file and get content
with open('./encryption_test/encrypt_decrypt_test/pass.txt', 'rb') as f:
    encrypted = f.read()

# decrypt the contents of the file
decrypted = fernet.decrypt(encrypted)

# open the text file and write the decrypted the content into the file
with open('./encryption_test/encrypt_decrypt_test/pass.txt', 'wb') as f:
    f.write(decrypted)
    