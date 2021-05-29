# program which gives 10 or 50 dollar notes


class ATM():

    # initialise instance variable
    def __init__(self):
        user = self.user()
        cal = self.cal(user, 0, 0)
        
    # function to prompt user for user input

    def user(self):
        withdraw = int(input("Enter withdrawal amount: "))
        return withdraw

    # function to calculator how many $50 or $10 to dispense
    def cal(self, num, counter1, counter2):
        # set counters to 0
        counter_10 = counter1
        counter_50 = counter2
        # set value to num
        value = num

        if value % 10 == 0:
            if (value - 50) > 0:
                value -= 50 
                counter_50 += 1
                print(counter_50)
                self.cal(value, counter_10, counter_50)
            elif (value - 10) > 10:
                value -= 10
                counter_10 += 1
                print(counter_10)
                self.cal(value, counter_10, counter_50)

            else:
                return counter_10, counter_50
        else:
            pass


if __name__ == "__main__":
    ATM()
