import sys, random

def calculator():
    print("Select a operation")
    choose = " "
    num1 = " "
    num2 = " "

    while choose == " ":
        try:
            choose = int(input("Please type 1 for Addition, 2 for subtraction, 3 for multiply, 4 for divide"))
        except ValueError:
            print("Please type a number only.")

    if choose == 1:

        while num1 == " ":
            try:
                num1 = int(input("Please type your first number below: "))
            except ValueError:
                print("Please type number only.")

        while num2 == " ":
            try:
                num2 = int(input("Please type your second number below: "))
            except ValueError:
                print("Please type number only.")

            print(num1 + num2)

    if choose == 2:

        while num1 == " ":
            try:
                num1 = int(input("Please type your first number below: "))
            except ValueError:
                print("Please type number only.")

        while num2 == " ":
            try:
                num2 = int(input("Please type your second number below: "))
            except ValueError:
                print("Please type number only.")

        print(num1 - num2)

    if choose == 3:

        while num1 == " ":
            try:
                num1 = int(input("Please type your first number below: "))
            except ValueError:
                print("Please type number only.")

        while num2 == " ":
            try:
                num2 = int(input("Please type your second number below: "))
            except ValueError:
                print("Please type number only.")

        print(num1 * num2)

    if choose == 4:

        while num1 == " ":
            try:
                num1 = int(input("Please type your first number below: "))
            except ValueError:
                print("Please type number only.")

        while num2 == " ":
            try:
                num2 = int(input("Please type your second number below: "))
            except ValueError:
                print("Please type number only.")

        print(num1 / num2)

    else:
        print("Something went wrong. Please tyr again later.")




calculator()
