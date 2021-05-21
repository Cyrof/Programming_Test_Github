# import lib
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# sub window class


class NewWindow(Toplevel):

    # initialise intances which creates new window
    def __init__(self, master=None):

        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")

        # call create_Widgets function 
        self.create_Widgets()

        # call check function
        self.check()

    # function to create widgets for sub window
    def create_Widgets(self):
        # create sub window label
        self.label = tk.Label(self, text="This is a sub window")
        self.label.pack()

        '''
        # create quit button 
        self.quit_btn = tk.Button(self.master, text="Quit", fg="red", command=self.destroy)
        self.quit_btn.pack(side=BOTTOM)
        '''
        
    # check function to check whether this sub window is open
    # If this sub window is open, main window cannot open another sub
    # window. Else window will proceed to open as per normal

    def check(self):
        self.transient(self.master)
        self.grab_set()
        self.master.wait_window(self)