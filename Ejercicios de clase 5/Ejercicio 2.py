'''
Desarrolle un programa que permita determinar la nota mayor,
la nota menor, la cantidad de aprobados y la cantidad de
reprobados de un grupo de alumnos. Muestre los resultados
obtenidos.

Nota: No se conoce la cantidad de alumnos.
La nota de aprobación es 70.
'''

print('Bienvenido')
notas = input('Ingrese la nota o escriba Terminar para ver los resultados: ')

mayor = 0
menor = 100
aprobados = 0
reprobados = 0

while notas != 'Terminar':
    notas = int(notas)
    if notas > mayor:
        mayor = notas

    if notas < menor:
        menor = notas

    if notas >= 70:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

    notas = input('Ingrese la nota o escriba Terminar para terminar: ')

print(f'La nota más alta es {mayor}')
print(f'La nota más baja es {menor}')
print(f'El total de alumnos aprobados es {aprobados}')
print(f'El total de alumnos reprobados es {reprobados}')
