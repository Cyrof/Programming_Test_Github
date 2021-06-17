from cryptography.fernet import Fernet
import csv

#generate random key 
key = Fernet.generate_key()

#create csv file to store key 
with open('./encryption_test/csv_test/key.csv', 'rb+') as f:
    f.write(key)
    f.close()

