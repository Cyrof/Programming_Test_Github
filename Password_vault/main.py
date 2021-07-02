import hashlib
from log import Log
from masterpass import Masterpass


class main:

    # set log to global
    global log

    # set keycheck and master to global
    global keyCheck
    global master

    # call log class and start logging
    start_logging = Log().file_check()
    log = Log().showlog()

    # call masterpass class
    master = Masterpass()
    keyCheck = master.checkFile()

    def __init__(self):
        pass

    def checkLog(self):
        if (log == 1) or (keyCheck == 0):
            master.user()
        else:
            self.login()

    def login(self):
        for x in range(3):
            ps = input("Enter masterpassword: ")
            encrpyted_ps = hashlib.sha256(ps.encode()).hexdigest()
            check = master.checker(encrpyted_ps)

            if check == True:
                break
            else:
                print("Wong password!")

if __name__ == "__main__":
    start = main().checkLog()
