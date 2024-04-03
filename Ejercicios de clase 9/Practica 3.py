# Práctica #3: Subprogramas y arreglos unidimensionales

titulos = []
copias = []

def registrar_libros():
    while True:
        titulo = input("Por favor ingrese el título de un libro (o escribe 'salir' para terminar): ")
        if titulo.lower() == 'salir':
            break
        while True:
            try:
                numero_copias = int(input(f"Defina el número de copias disponibles para '{titulo}': "))
                if numero_copias >= 0:
                    break
                else:
                    print("Por favor ingresa un número válido de copias (mayor o igual a 0).")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        titulos.append(titulo)
        copias.append(numero_copias)

def calcular_promedio_copias():
    if copias:
        promedio = sum(copias) / len(copias)
        print(f"El promedio de copias disponibles es: {promedio:.2f}")
    else:
        print("No hay libros registrados para calcular un promedio.")

def evaluar_disponibilidad():
    if copias:
        promedio = sum(copias) / len(copias)
        if promedio >= 10:
            disponibilidad = "Suficiente"
        elif 5 <= promedio < 10:
            disponibilidad = "Moderada"
        else:
            disponibilidad = "Baja"
        print(f"La disponibilidad de libros es {disponibilidad}.")
        for titulo, copia in zip(titulos, copias):
            print(f"Titulo: {titulo}, Copias disponibles: {copia}")
    else:
        print("No hay libros registrados para evaluar la disponibilidad.")

def mostrar_menu():
    while True:
        print("\nBienvenido al sistema de gestión de libros de la Biblioteca virtual")
        print("\nPor favor seleccione una de las siguientes opciones:")
        print("1. Registrar libros")
        print("2. Calcular el promedio de las copias disponibles")
        print("3. Evaluar disponibilidad de libros")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            registrar_libros()
        elif opcion == '2':
            calcular_promedio_copias()
        elif opcion == '3':
            evaluar_disponibilidad()
        elif opcion == '4':
            print("Saliendo del programa de gestión de biblioteca...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción del 1 al 4.")

# Llamada a la función que muestra el menú
mostrar_menu()

