# This is a small bank simulator

balance = 0.0
option = 0

while option != str(4):

    print('''
        ********** MENU *********
        1. Check balance
        2. Deposit
        3. Withdrawl
        4. Exit
        *************************
        
        Please enter your option
        ''')

    option = input()

    if option == str(1):
        print("This is your balance: " + str(balance))
    elif option == str(2):
        print("How much do you want to deposit? ")
        deposit = float(input())
        balance = balance + deposit
    elif option == str(3):
        print("How much do you want to withdrawl? ")
        withdrawl = float(input())
        balance = balance - withdrawl

print("Thank you and good bye")
