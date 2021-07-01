#!/usr/bin/python3
from getpass import getpass
import os
# getpass is a library that hide the user input in the prompt.

USERNAME = '51614'
PASSWORD = USERNAME[::-1]   # '41615'

menuOption = {
'1': "Cambiar contraseña",
'2': "Ingresar coordenadas actuales",
'3': "Ubicar zona wifi más cercana",
'4': "Guardar archivo con ubicación cercana",
'5': "Actualizar registros de zonas wifi desde archivo",
'6': "Elegir opción de menú favorita",
'7': "Cerrar sesión"
}

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
        #Invoke subFunction for menu
        menuOptions()

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


def menuOptions():

    sesion = True
    contador = 3
    displayMenu()   #call function for display main menu

    # validate state of sesion
    while sesion:

        option = input("Elija una opción\n")

        if isPosibleOption(option):
            contador = 3

        if option == '1':
            print("Usted ha elegido la opción 1")
            sesion = False

        elif option == '2':
            print("Usted ha elegido la opción 2")
            sesion = False

        elif option == '3':
            print("Usted ha elegido la opción 3")
            sesion = False

        elif option == '4':
            print("Usted ha elegido la opción 4")
            sesion = False

        elif option == '5':
            print("Usted ha elegido la opción 5")
            sesion = False

        elif option == '6':
            favorito = input("Seleccione opción favorita\n")
            if isPosibleFavorite(favorito):
                if adivinanzas():
                    # reorder menu whit the select option
                    previos_option_value = menuOption.get('1')
                    new_order = menuOption.get(favorito)
                    menuOption.update({'1': new_order,
                        favorito: previos_option_value})

                    # clean console
                    clearConsole()
                    displayMenu()
                else:
                    print("Error")
            else:
                print("Error")
                sesion = False

        elif option == '7':
            print("Hasta pronto")
            sesion = False

        else:
            print("Error")
            contador -= 1
            if contador == 0:
                sesion = False

# Helper Function for displays the main menu
def displayMenu():
    for key, value in menuOption.items():
        print(f'{key}. {value}')

# Helper Function for validate the correct options in main menu
def isPosibleOption(favorite):
    return favorite.isdigit() and int(favorite) >= 1 and int(favorite) <= 7

# Helper Function for validate the correct options inside menu 6
def isPosibleFavorite(favorite):
    return favorite.isdigit() and int(favorite) >= 1 and int(favorite) <= 5

# Helper Function to check the answers of guessings
def adivinanzas():
    last_character = USERNAME[-1]
    second_last_char = USERNAME[-2]

    acertijo1 = input("Para confirmar por favor responda: Cuando te pones a contar por mi tienes que empezar. Quien soy? \n")
    if acertijo1 != second_last_char:
        return False

    acertijo2 = input("Para confirmar por favor responda: Soy un numero y no miento que tengo forma de asiento. Quien soy? \n")
    if acertijo2 != last_character:
        return False

    return  True


# Helper function for clear the console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# Invoke the Main Function
userData()
