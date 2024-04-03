'''
Desarrolle un programa que eleve un número a una potencia.

Nota: Debe utilizar instrucciones de lectura y operaciones
aritméticas
'''

base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))

numero_con_potencia = base ** exponente

print(f'El número elevado a la potencia es {base}^{exponente}' \
      f' y su resultado es {numero_con_potencia}')
