'''
Desarrolle un programa intercambie el valor de las edades de Luis y
Pedro y muestre las edades luego de realizado el intercambio.
Nota: Considere que las variables sólo pueden almacenar un valor
a la vez, por lo que el asignar un nuevo valor provocará la pérdida
del valor anterior.
'''

edad_luis = int(input('Ingrese la edad de Luis: '))
edad_pedro = int(input('Ingrese la edad de Pedro: '))

cambio_luis = edad_pedro
cambio_pedro = edad_luis

print(f'La edad de Luis es: {cambio_luis}')
print(f'La edad de Pedro es: {cambio_pedro}')


