#!/usr/bin/python3
import os
import math
import numpy as np
from getpass import getpass
# getpass is a library that hide the user input in the prompt.

USERNAME = '51614'
user_mintic = 'Tripulante2022'
password = USERNAME[::-1]   # '41615'
LATITUD_SUP = 6.284
LATITUD_INF = 6.077
LONGITUD_OR = -75.841
LONGITUD_OCC = -76.049
coordinates = None
wifi_zone = np.array(
    [[6.124, -75.946, 1035],
    [6.125, -75.966, 109],
    [6.135, -75.976, 31],
    [6.144, -75.836, 151]]) #revisar longitud
work_coordenates = [None, None]
house_coordenates = [None, None]
park_coordenates =[None, None]
session = True


# userData is a Function to catch the user name and password
def userData():

    # Welcome Message
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

    # Variables to cacth the input name from user
    # Conditional validation for name input
    name = input("Please enter your User Name:\n")
    if name == user_mintic:
        print("Este fue mi primer programa y vamos por más")
        return 0

    if name != USERNAME:
        print("Error")
        return 0

    user_password = getpass("Please enter your Password:\n")
    if user_password != password:
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


################ MENU OPTION 1 #############
# Helper function for for change password
def changePassword(_option):
    global session
    global password

    confirm_password = input("Favor ingrese su contaseña actual:\n")
    if  password != confirm_password:
        print("Error")
        session = False
        return

    new_password = input("Ingrese su nueva contraseña: \n")
    if new_password == password:
        print("Error")
        session = False
        return

    password = new_password
    clearConsole()
    displayMenu()


################ MENU OPTION 2 #############
def createCoordinates():
    global coordinates
    global session
    global work_coordenates
    global house_coordenates
    global park_coordenates


    try:
        work_latitud = float(input("Ingrese la latitud de su trabajo:\n"))
        if not validateLatitud(work_latitud):
            return
        work_coordenates[0]= work_latitud

        work_longitud = float(input("Ingrese la longitud de su trabajo:\n"))
        if not validateLongitud(work_longitud):
            return
        work_coordenates[1] = work_longitud

        house_latitud = float(input("Ingrese la latitud de su casa:\n"))
        if not validateLatitud(house_latitud):
            return
        house_coordenates[0]= house_latitud

        house_longitud = float(input("Ingrese la longitud de su casa:\n"))
        if not validateLongitud(house_longitud):
            return
        house_coordenates[1] = house_longitud

        park_latitud = float(input("Ingrese la latitud del parque:\n"))
        if not validateLatitud(park_latitud):
            return
        park_coordenates[0]= park_latitud

        park_longitud = float(input("Ingrese la longitud del parque:\n"))
        if not validateLongitud(park_longitud):
            return
        park_coordenates[1]= park_longitud
    except ValueError:
        print("Error")
        session = False
        return

    coordinates = np.array([work_coordenates, house_coordenates, park_coordenates])
    clearConsole()
    displayMenu()


def validateLatitud(latitud):
    global session
    if latitud < LATITUD_INF or latitud > LATITUD_SUP:
        print("Error coordenada")
        session = False
        return False
    else:
        return True

def validateLongitud(longitud):
    global session
    if longitud > LONGITUD_OR or longitud < LONGITUD_OCC:
        print("Error coordenada")
        session = False
        return False
    else:
        return True

def promedioLatitud():
    global coordinates
    south = 1
    latitude_south = coordinates[0][0]

    for i in range(1, len(coordinates)):
        if coordinates[i][0] < latitude_south:
            latitude_south = coordinates[i][0]
            south += 1

    return south

def promedioCoordenates():
    global coordinates

    promedio = [0,0]
    promedio_latitud = (coordinates[0][0] + coordinates[1][0] + coordinates[2][0]) / 3
    promedio_longitud = (coordinates[0][1] + coordinates[1][1] + coordinates[2][1]) / 3

    latitud = float("{:.3f}".format(promedio_latitud))
    longitud = float("{:.3f}".format(promedio_longitud))

    promedio[0] = latitud
    promedio[1] = longitud

    return promedio


def updateCoordenates(_option):
    global session
    global coordinates
    validate_coordenates = np.all(coordinates)

    if validate_coordenates:

        print(f'coordenada [latitud, longitud] 1 : {coordinates[0].tolist()}')
        print(f'coordenada [latitud, longitud] 2 : {coordinates[1].tolist()}')
        print(f'coordenada [latitud, longitud] 3 : {coordinates[2].tolist()}')
        print(f"La coordenada {promedioLatitud()} es la que esta ubicada más al sur")
        print(f"La coordenada promedio de todos los puntos es: {promedioCoordenates()}")

        try:
            update_option = input("Presione 1, 2 o 3 para actualizar la respectiva coordenada\n"
                "Presione 0 para regresar al menu\n")


            if update_option == "0":
                displayMenu()

            elif update_option == "1":
                update_work()

            elif update_option == "2":
                update_house()

            elif update_option == "3":
                update_park()

            else:
                print("Error actualización")
                session = False
                return
        except ValueError:
            print("Error")
            session = False
            return
    else:
        createCoordinates()


def update_coordenates():

    latitud = float(input("Ingrese la latitud:\n"))
    if not validateLatitud(latitud):
        return

    longitud = float(input("Ingrese la longitud:\n"))
    if not validateLongitud(longitud):
        return

    return [latitud, longitud]

def update_work():
    global coordinates
    coordinates[0] = np.array(update_coordenates())

    clearConsole()
    displayMenu()

def update_house():
    global coordinates
    coordinates[1] = np.array(update_coordenates())

    clearConsole()
    displayMenu()

def update_park():
    global coordinates
    coordinates[2] = np.array(update_coordenates())

    clearConsole()
    displayMenu()


################ MENU OPTION 3 #############
def fetchWifis():
    global wifi_zone

    place_1 = wifi_zone[0].tolist()
    place_2 = wifi_zone[1].tolist()
    place_3 = wifi_zone[2].tolist()
    place_4 = wifi_zone[3].tolist()

    return [place_1, place_2, place_3, place_4]


def setHaversineInPlace(ubicacion_1, ubicacion_2):

    latitud_1 = ubicacion_1[0]
    longitud_1 = ubicacion_1[1]

    latitud_2 = ubicacion_2[0]
    longitud_2 = ubicacion_2[1]


    radio = math.pi/180
    distancia_latitudes = latitud_2 - latitud_1
    distancia_longitudes = longitud_2 - longitud_1
    R = 6372.795477598
    a = (math.sin(radio * distancia_latitudes / 2))**2 + math.cos(radio * latitud_1) * math.cos(radio * latitud_2)*(math.sin(radio * distancia_longitudes / 2))**2

    distancia = 2 * R * math.asin(math.sqrt(a)) # distancia en kilometros
    distancia *= 1000 #distancia en metros

    distancia_metros = math.trunc(distancia)
    ubicacion_2.append(distancia_metros)

    return ubicacion_2


def shorterDistances(places_with_distance):

    places_with_distance = sorted(places_with_distance,
        key=lambda place_with_distance: place_with_distance[3])


    small_distance = places_with_distance[0]
    second_small_distance = places_with_distance[1]

    return small_distance, second_small_distance


def arribal_time(place_coordenates):

    speed_moto =  19.44
    speed_bicicleta =  3.33

    time_moto = place_coordenates[3] / speed_moto
    time_moto = int(time_moto)
    time_bicicleta = place_coordenates[3] / speed_bicicleta
    time_bicicleta = int(time_bicicleta)

    return time_moto, time_bicicleta



def followDirection(user_coordenates, place_coordenates):

    direccion_latitud = None
    direccion_longitud = None


    if user_coordenates[1] > place_coordenates[1]:
        direccion_longitud = 'occidente'
    else:
        direccion_longitud = 'oriente'


    if user_coordenates[0] > place_coordenates[0]:
        direccion_latitud = 'sur'
    else:
        direccion_latitud = 'norte'


    moto, bicicleta = arribal_time(place_coordenates)

    print(f'Para llegar a la zona wifi dirigirse primero al {direccion_longitud} y luego hacia el {direccion_latitud}')
    print(f'El tiempo promedio en llegar a la zona wifi en moto es de {moto} segundos')
    print(f'El tiempo promedio en llegar a la zona wifi en bicicleta es de {bicicleta} segundos')


    try:
        back_to_menu = input("Presione 0 para salir\n")
        if back_to_menu == "0":
            displayMenu()
    except ValueError:
        print("Error")
        session = False
        return


def searchWifi(coords_to_compare):
    global session
    global coordinates
    places = fetchWifis()
    places_with_distance = list(
        map(lambda place: setHaversineInPlace(coords_to_compare, place), places))


    min_distance, second_min_distance = shorterDistances(places_with_distance)

    print("Zonas wifi cercanas con menos usuarios")
    print(f'La zona Wifi 1: ubicada en {min_distance[:2]} a {min_distance[3]} metros, tiene en promedio {int(min_distance[2])} usuarios')
    print(f'La zona Wifi 2: ubicada en {second_min_distance[:2]} a {second_min_distance[3]} metros, tiene en promedio {int(second_min_distance[2])} usuarios')


    #continuar para elejir indicaciones de coordenadas
    try:
        option_location = input("Elija 1 o 2 para recibir indicaciones de llegada\n")

        if option_location == "1":
            followDirection(coords_to_compare, min_distance)

        elif option_location == "2":
            followDirection(coords_to_compare, second_min_distance)

        else:
            print("Error zona wifi")
            session = False
            return
    except ValueError:
        print("Error")
        session = False
        return


def searchNearhWifiZone(_option):
    global session
    global coordinates
    validate_coordenates = np.all(coordinates)

    if validate_coordenates:
        print(f'coordenada [latitud, longitud] 1 : {coordinates[0].tolist()}')
        print(f'coordenada [latitud, longitud] 2 : {coordinates[1].tolist()}')
        print(f'coordenada [latitud, longitud] 3 : {coordinates[2].tolist()}')

        try:
            current_location = input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión\n")

            if current_location == "1":
                searchWifi(coordinates[0].tolist())

            elif current_location == "2":
                searchWifi(coordinates[1].tolist())

            elif current_location == "3":
                searchWifi(coordinates[2].tolist())

            else:
                print("Error ubicación")
                session = False
                return
        except ValueError:
            print("Error")
            session = False
            return

    else:
        print("Error sin registro de coordenadas")
        session = False


################ MENU OPTION 4 #############
def saveFile(option):
    print(f"Usted ha elegido la opción {option}")


################ MENU OPTION 5 #############
def updateFiles(option):
    print(f"Usted ha elegido la opción {option}")


################ MENU OPTION 6 #############
def changeFavorite(_option):
    favorito = input("Seleccione opción favorita\n")
    if isPosibleFavorite(favorito):
        if adivinanzas():
            # reorder menu whit the select option
            previos_option_value = menuOption.get('1') # get actual element in posicion with key 1
            new_order = menuOption.get(favorito) # get value of opticion user
            menuOption.update({'1': new_order,
                favorito: previos_option_value}) # reorder update = position key 1 --> user election

            # clean console
            clearConsole()
            displayMenu()
        else:
            print("Error")
    else:
        print("Error")
        global session
        session = False

################ MENU OPTION 7 #############
def endSession(_option):
    print("Hasta pronto")
    global session
    session = False


################ MENU OPTION 2021 #############
def whereIam():
    global session
    try:
        where_user_is = float(input("Dame una latitud y te diré cual hemisferio es…\n"))
        if where_user_is > 0 :
            print('Usted está en hemisferio norte')
        else:
            print('Usted está en hemisferio sur')

        session = False
    except ValueError:
        print("Error")
        session = False
        return


################ MAIN MENU #############
menuOption = {
    '1': {
        'title': "Cambiar contraseña",
        'action': changePassword
    },
    '2': {
        'title': "Ingresar coordenadas actuales",
        'action': updateCoordenates
    },
    '3': {
        'title': "Ubicar zona wifi más cercana",
        'action': searchNearhWifiZone
    },
    '4': {
        'title': "Guardar archivo con ubicación cercana",
        'action': saveFile
    },
    '5': {
        'title': "Actualizar registros de zonas wifi desde archivo",
        'action': updateFiles
    },
    '6': {
        'title': "Elegir opción de menú favorita",
        'action': changeFavorite
    },
    '7': {
        'title': "Cerrar sesión",
        'action': endSession
    }
}


def menuOptions():
    global session
    contador = 3
    displayMenu()   #call function for display main menu

    # validate state of session
    while session:

        option = input("Elija una opción\n")
        if option == '2021':
            whereIam()

        elif isPosibleOption(option):
            contador = 3

            option_data = menuOption.get(option)
            option_data.get('action')(option)
        else:
            print("Error")
            contador -= 1
            if contador == 0:
                session = False

# Helper Function for displays the main menu
def displayMenu():
    for key, value in menuOption.items():
        print(f'{key}. {value.get("title")}')

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
