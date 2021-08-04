# import lib
import os 

# log class
class Log:
    
    # default constructor
    def __init__(self):
        pass

    # read from file
    def file(self):
        with open('./log.txt', 'r+') as f:
            content = f.read()
            counter = int(content)
            self.logging(counter)

    # log to file
    def logging(self, counter):
        counter += 1
        with open('./log.txt', 'w+') as f:
            f.write(str(counter))

    # check if file is empty
    def file_check(self):
        check = os.stat('./log.txt').st_size
        if check == 0:
            counter = 0
            self.logging(counter)
        else: 
            self.file()
    
    # showlog from file
    def showlog(self):
        with open('./log.txt', 'r+') as f:
            content = f.read()
            counter = int(content)
        return counter

    # reset log file
    def reset(self):
        with open('./log.txt', 'w+') as f:
            f.write("")


