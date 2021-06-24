import hashlib

#generate sha256 key for word
key = 'doraemon'
encrypt = hashlib.sha256(key.encode()).hexdigest()
print(encrypt)

#user input to check if master pass match sha256 key 
master_pass = input("Enter master password: ")
encrypt_master = hashlib.sha256(key.encode()).hexdigest()

if encrypt_master == encrypt:
    print("correct master password.")


