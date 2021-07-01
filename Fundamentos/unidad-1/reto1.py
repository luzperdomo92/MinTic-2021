#!/usr/bin/python3
from getpass import getpass
# getpass is a library that hide the user input in the prompt.

USERNAME = '51614'
PASSWORD = USERNAME[::-1]   # '41615'


# userData is a Function to catch the user name and password
def userData():

    # Welcome Message
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

    # Variables to cacth the input name from user
    # Conditional validation for name input
    name = input("Please enter your User Name:\n")
    if name != USERNAME:
        print("Error")
        return 0

    password = getpass("Please enter your Password:\n")
    if password != PASSWORD:
        print("Error")
        return 0

    # Invoke the Helper Function
    capcha()


# Helper function for generate the capcha.
def capcha():

    # variable that store the value of last three character
    last_3_chars = USERNAME[-3:]

    # store in variable the result of helper function --> 1
    second_last_char = validationCapcha()
    result_capcha_value = int(last_3_chars) + int(second_last_char)

    # user output the operaction and the result is stored in the variable
    result_capcha_user = int(input(f'{last_3_chars} + {second_last_char} =\n'))

    # comparation the result
    if result_capcha_user != result_capcha_value:
        print('Error')
    else:
        print('Sesión iniciada')

    return 0


# Helper function for validate operations for generation the capcha.
def validationCapcha():

    # variable that store de value 1
    second_last_char = int(USERNAME[-2])

    test_capcha_1 = int((6 + 4) / 5 - 1)
    test_capcha_2 = int((6 + 5 + 1) / 6 - 1)
    test_capcha_3 = int((6 * 5) / 5 - 5)

    if(test_capcha_1 == second_last_char and test_capcha_2 == second_last_char
            and test_capcha_3 == second_last_char):
        return second_last_char


# Invoke the Main Function
userData()
