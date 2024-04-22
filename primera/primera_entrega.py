usuarios = {}


def registrar_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios:
        print("El usuario ya existe, ingrese otro")
    else:
        usuarios[usuario] = contraseña
        print("Usuario ingresado correctamente")


def mostrar_datos():
    print("Usarios registrados")
    for usuario, contraseña in usuarios.items():
        print(f"Usuario: {usuario} Contraseña: {contraseña}")


def login_usuario():
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese su usario para ingresar: ")
        contraseña = input("Ingrese su contraseña para ingresar: ")
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("Bienvenido!")
            break
        else:
            intentos += 1
            if intentos < 3:
                print("Usuario o contraseña Incorrectos")
                print(f"Intento {intentos} de 3")
            else:
                print("Usuario o Contraseña incorrectos. Se han terminados los intentos")


while (True):
    print("\nOpciones: ")
    print("1. Registrar un nuevo usuario")
    print("2. Mostrar usuarios registrados")
    print("3. Login de usuario")
    print("4. Salir")
    opciones = input("Ingrese una opción: ")

    if opciones == "1":
        registrar_usuario()
    elif opciones == "2":
        mostrar_datos()
    elif opciones == "3":
        login_usuario()
    elif opciones == "4":
        print("Hasta la próxima ")
        break
    else:
        print("Opción no valida. Por favor, intente nuevamente")
