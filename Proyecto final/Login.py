def verificar_credenciales(usuario, contraseña):
    # Credenciales predefinidas
    usuario_correcto = "admin"
    contraseña_correcta = "1234"

    return usuario == usuario_correcto and contraseña == contraseña_correcta

def login():
    print("Bienvenido al sistema de facturación de la empresa X. Escribe 'salir' en cualquier momento para salir.")

    while True:
        usuario = input("Introduce tu nombre de usuario: ")
        if usuario.lower() == 'salir':
            print("Saliendo del sistema de login...")
            break

        contraseña = input("Introduce tu contraseña: ")
        if contraseña.lower() == 'salir':
            print("Saliendo del sistema de login...")
            break

        if verificar_credenciales(usuario, contraseña):
            print("Login exitoso. Bienvenido al sistema.")
            break
        else:
            print("Error. Usuario o contraseña incorrectos. Intenta de nuevo o escribe 'salir' para salir.")

if __name__ == "__main__":
    login()
