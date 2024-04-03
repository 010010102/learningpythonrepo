'''
Desarrolle un programa que le solicite al usuario
sus ingresos mensuales y sus gastos mensuales
por alimentación.
Con esta información el programa debe mostrar
el porcentaje que gasto que corresponde al
rubro de alimentación y el porcentaje que
queda disponible para otros rubros.
'''

ingresos_mensuales = float(input("Por favor escriba el monto total de sus ingresos mensuales: "))
gastos_de_alimentacion = float(input("Por favor escriba el monto total de sus gastos mensuales de alimentación: "))

porcentaje_gastos_alimentacion = (gastos_de_alimentacion / ingresos_mensuales) * 100
porcentaje_otros_rubros = 100 - porcentaje_gastos_alimentacion

print(f"El porcentaje destinado a alimentación es: {porcentaje_gastos_alimentacion:.2f}%")
print(f"El porcentaje disponible para otros rubros es: {porcentaje_otros_rubros:.2f}%")
