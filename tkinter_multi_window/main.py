# import lib
import secondWindow
import tkinter as tk
from tkinter import *
from tkinter.ttk import *


# main class
class Main(tk.Frame):

    # initialise instance variables which create main window
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_Widgets()

    # function to create all widgets in main function
    def create_Widgets(self):
        # create label
        self.label = Label(self, text="This is the main window")
        self.label.pack(side=TOP, pady=10)

        # create button to open another window
        self.btn = tk.Button(self, text="Click me!")
        self.btn.bind("<Button>", lambda e: self.new_Window())
        self.btn.pack()

        # create a quit button
        self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        self.quit.pack(side=BOTTOM)

    # function to open another window using button
    def new_Window(self):
        new = secondWindow.NewWindow(self.master)
        

# initialise Tk object
root = Tk()
root.geometry("200x200")
app = Main(master=root)
app.mainloop()

