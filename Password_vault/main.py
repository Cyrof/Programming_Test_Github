import hashlib
import time as t
from error import *
from log import Log
from masterpass import Masterpass
from menu import Menu


class main:

    # set log to global
    global log

    # set keycheck and master to global
    global keyCheck
    global master

    # set menu to global
    global menu

    # call log class and start logging
    start_logging = Log().file_check()
    log = Log().showlog()

    # call masterpass class
    master = Masterpass()
    keyCheck = master.checkFile()

    # call menu class
    menu = Menu()

    def __init__(self):
        pass

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

    def login(self):
        for x in range(3):
            ps = input("Enter masterpassword: ")
            print("")
            encrpyted_ps = hashlib.sha256(ps.encode()).hexdigest()
            check = master.checker(encrpyted_ps)

            if check == True:
                self.Main_menu()
                break
            else:
                print("Wong password!")

    def Main_menu(self):
        while(True):
            choice = menu.mainMenu()
            print(choice)

            if choice == 3:
                break
            else:
                self.processing(choice=choice)
                continue
        
    def processing(self, choice):
        try:
            if choice == 1:
                pass
            elif choice == 2:
                pass
            else:
                raise NoValueFound
        except NoValueFound:
            print("No value Found")
                

if __name__ == "__main__":
    start = main().checkLog()
