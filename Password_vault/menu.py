
class Menu:

    def __init__(self):
        pass

    def firstcheck(self):
        choice = input("\nDo you want to continue to login? [y/n]: ")
        
        if choice.lower() == "y":
            return True
        else:
            return False

    def mainMenu(self):
        print("\nEnter new credentials \t[1]")
        print("View all credentials \t[2]")
        print("Exit \t\t\t[3]")
        choice = int(input("Enter choice: "))
        return choice
        