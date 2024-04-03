'''
Desarrolle un programa que le solicite un
número al usuario y calcule el cuadrado
y el cubo de este.
'''

total = float(input("Ingrese un número: ")) #He usado float en caso de requerir decimales

cuadrado = total ** 2
cubo = total ** 3

'''
El ejercicio no especifica si requiere print
pero lo agrego para verificación.
'''

print("El cuadrado del número digitado es: ", (cuadrado))
print("El cubo del número digitado es: ", (cubo))
