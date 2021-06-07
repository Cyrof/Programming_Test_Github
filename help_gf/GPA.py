# app to calculator gpa of 5 module

# initialise variables
string = "Module"
total_gp = 0
total_credit = 0

# prompt user 5 time for input
# each prompt to ask user for their credit score and gpa
# for loop to prompt user
'''
for x in range(5):
    # for (int i = 0; i < 5; i++)

    # prompt user for user input
    credit_score = float(
        input("Enter the credit for %s %d : " % (string, x + 1)))
    mod_gpa = float(input("Enter you GPA for %s %d : " % (string, x + 1)))

    # add cedit score and gp to total
    total_credit += credit_score
    total_gp += (mod_gpa * credit_score)
'''
x = 0

while x != 5:

    # prompt user for user input
    credit_score = float(
        input("Enter the credit for %s %d : " % (string, x + 1)))
    mod_gpa = float(input("Enter you GPA for %s %d : " % (string, x + 1)))

    # add cedit score and gp to total
    total_credit += credit_score
    total_gp += (mod_gpa * credit_score)
    x += 1

# cal gpa for 5 mod
gpa = total_gp / total_credit

# print output
print("Your cumulative GPA for 5 modules are %f" % (gpa))
