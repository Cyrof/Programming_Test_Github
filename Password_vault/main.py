# import lib
import hashlib
import time as t
from error import *
from log import Log
from masterpass import Masterpass
from menu import Menu
from Encrypt_decrypt import Cipher

# main class
class main:

    # set log to global
    global log

    # set keycheck and master to global
    global keyCheck
    global master

    # set menu to global
    global menu

    # set cipher to global
    global cipher

    # call log class and start logging
    start_logging = Log().file_check()
    log = Log().showlog()

    # call masterpass class
    master = Masterpass()
    keyCheck = master.checkFile()

    # call menu class
    menu = Menu()

    # Cipher
    cipher = Cipher()

    # default constructor
    def __init__(self):
        pass

    # check log file and key file if any is empty
    def checkLog(self):
        if (log == 1) or (keyCheck == 0):
            master.user()
            t.sleep(2)
            check = menu.firstcheck()
            if check == True:
                self.login()
            else:
                pass

        else:
            self.login()

    # login function which prompt user for master ps
    def login(self):
        for x in range(3):
            ps = input("Enter masterpassword: ")
            print("")
            encrpyted_ps = hashlib.sha256(ps.encode()).hexdigest()
            check = master.checker(encrpyted_ps)

            if check == True:
                cipher.getHash()
                self.Main_menu()
                break
            else:
                print("Wrong password!")

    # display menu for user
    def Main_menu(self):
        while(True):
            choice = menu.mainMenu()
            print(choice)

            if choice == 0:
                break
            elif choice != None:
                self.processing(choice=choice)
                continue
            else:
                continue
        
    # process choice from Main_menu function
    def processing(self, choice):
        try:
            if choice == 1:
                cipher.showKey()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            else:
                raise NoValueFound
        except NoValueFound:
            print("No value Found")
                

if __name__ == "__main__":
    start = main().checkLog()
