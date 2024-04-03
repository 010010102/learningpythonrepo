'''
Realice un programa que dada
la base y la altura de un rectángulo,
calcule el área y el perímetro de este.
'''

base = float(input("Ingrese la base: ")) #He usado float en caso de requerir decimales
altura = float(input("Ingrese un la altura: ")) #He usado float en caso de requerir decimales

area = base * altura
perimetro = (base + altura) * 2

print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)
