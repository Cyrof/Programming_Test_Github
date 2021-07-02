from log import Log

class main:
    
    #set log to global 
    global log

    # call log class and start logging 
    start_logging = Log().file_check()
    log = Log().showlog()

    def __init__(self):
        pass

    def checkLog(self):
        if log == 0:
            pass
        else:
            pass


    
    



if __name__ == "__main__": 
    start = main()