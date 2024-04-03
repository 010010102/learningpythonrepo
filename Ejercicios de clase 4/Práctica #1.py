'''
Acividad:
Desarrollar un programa en Python que permita al usuario
ingresar las longitudes de los tres lados de un triángulo
y determine el tipo de triángulo formado por esas longitudes.



Práctica #1: Estructuras de Selección
Nombre: Johanan Campos
Fecha: 2024-01-06
'''

# Solicita al usuario la longitud los tres lados pertenecientes a un triángulo
lado1 = int(input('Por favor ingrese la longitud del primer lado del triángulo: '))
lado2 = int(input('Por favor ingrese la longitud del segundo lado del triángulo: '))
lado3 = int(input('Por favor ingrese la longitud del tercer lado del triángulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1: #Acá valido que se pueda hacer un triángulo si no cumple se va al else
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
else:
    print("Las longitudes ingresadas no pueden formar un triángulo.")
