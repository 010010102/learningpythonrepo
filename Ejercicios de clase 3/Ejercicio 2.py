'''
El programa calculará el de la suma, la resta, la multiplicación y la
división de dos números y mostrará los resultados obtenidos.
Nota: Considere que, si ingresamos un cero como segundo
valor, obtendremos un error durante la ejecución del
programa. En próximas lecciones veremos cómo controlar este
'''

primer_numero = float(input('Por favor ingrese el primer número: '))
segundo_numero = float(input('Por favor ingrese el segundo número: '))

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
division = primer_numero / segundo_numero

print(f'El total de la suma de ambos números es {suma}')
print(f'El total de la resta de ambos números es {resta}')
print(f'El total de la multiplicacion de ambos números es {multiplicacion}')
print(f'El total de la division de ambos números es {division}')
