#Bibliotecas
import getpass

#26. Crear sistema de login simple
base_datos = {}

def elementos_vacios(elementos):
    if not elementos:
        print("\nInvalido. La entrada de los elementos no puede estar vacia.")
        exit()

def continuar_programa():
    continuar = input("\n¿Desea continuar con el programa?, (s,n): ").strip().lower()
    if continuar in ("s", "si"):
        return True
    else:
        print("\nEl programa a terminado.")
        return False

'''Tres funciones, la tercera principal. Funcion 1 - Login, Funcion 2 - Register, Funcion 3 - Main. '''
data_base = {}

def Login():
    User_name = input("\nUserName: ").strip()
    elementos_vacios(User_name)

    Password = input("\nPassword: ").strip()
    elementos_vacios(Password)

    if User_name and Password in data_base:
        print("\n¡Acceso concedido!")
    else:
        print("\nInvalido. El usuario ingresado no existe.")

    return User_name, Password

def Register():
    enter_username = input("\nRegister UserName: ").strip()
    elementos_vacios(enter_username)

    if enter_username in data_base:
        print("\nEl nombre de usuario ya existe. Ingrese otro.")
    else:
        enter_cellphone_number = input("\nRegister Cellphone Number: ").strip()
        elementos_vacios(enter_cellphone_number)

        enter_email = input("\nRegister Email: ").strip()
        elementos_vacios(enter_email)
        
        enter_password = input("\nRegister Password: ").strip()
        elementos_vacios(enter_password)

    if enter_password in data_base:
        print("\nLa contraseña ya existe. Ingrese otra.")
    else:
        data_base[enter_username] = enter_password

    return enter_username, enter_cellphone_number, enter_email, enter_password

def Main():
    while True:
        print("\n--- Sing Up ---")
        print("1. Login")
        print("2. Register")
        print("3. Salir")

        opciones = input("\nElige una de las siguientes opciones, por favor: ").strip()
        if opciones == "1":
            Login()
        elif opciones == "2":
            Register()
        elif opciones == "3":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción invalida. Eliga una de las opciones existentes.")

        if not continuar_programa():
            break

if __name__ == "__main__":
    Main()
