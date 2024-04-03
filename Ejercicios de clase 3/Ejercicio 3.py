'''
Elabore un programa que calcule y muestre el área y el perímetro de un
cuadrado.
Nota: Para realizar los cálculos requiere conocer la medida del lado del
cuadrado.
'''

tamano_de_lados = float(input('Por favor escriba el tamaño de los lados del cuadrado: '))

area_del_cuadrado = tamano_de_lados ** 2
perimetro_del_cuadrado = tamano_de_lados * 4

print(f'El área del cuadrado es: {area_del_cuadrado}')
print(f'El perímetro del cuadrado es: {perimetro_del_cuadrado}')
