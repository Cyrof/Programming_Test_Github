# menu class
class Menu:

    # default constructor
    def __init__(self):
        pass

    # first menu after creating master ps
    def firstcheck(self):
        choice = input("\nDo you want to continue to login? [y/n]: ")

        if choice.lower() == "y":
            return True
        else:
            return False

    # main menu function
    def mainMenu(self):
        print("\n[1] Enter new Password")
        print("[2] View all Password")
        print("[3] Delete")
        print("[0] Exit")

        try:
            choice = int(input("Enter choice: "))
            return choice
        except ValueError:
            print("Not valid choice")
            return None