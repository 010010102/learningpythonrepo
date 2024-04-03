'''
Se requiere analizar las estaturas de los N niños de una escuela y extraer la siguiente
estadística:
• Cantidad de niños que miden menos de 100 cm.
• Cantidad de niños que miden entre 100 y 120 cm.
• Cantidad de niños que miden entre 121 y 130 cm.
• Cantidad de niños que miden entre 131 y 140 cm.
• Cantidad de niños que miden más de 140 cm.
• Promedio de estaturas.
• Muestre los resultados obtenidos. 
'''

print('Bienvenido al sistema de promedio de estaturas')
print('Ac[a podrá ingresar las estaturas de múltiples niños para generar resultados totales')

menor_a_100 = 0
entre_100_120 = 0
entre_121_130 = 0
entre_131_140 = 0
mayor_que_140 = 0
suma_de_estaturas = 0
contador_de_ninos = 0

while True:
    estatura = input("Por favor ingrese la estatura del niño en cm o escriba salir para terminar: ")
    if estatura.lower() == 'salir':
        break
    if int(estatura) < 100:
        menor_a_100 += 1
    elif 100 <= int(estatura) <= 120:
        entre_100_120 += 1
    elif 121 <= int(estatura) <= 130:
        entre_121_130 += 1
    elif 131 <= int(estatura) <= 140:
        entre_131_140 += 1
    else:
        mayor_que_140 += 1

    suma_de_estaturas += int(estatura)
    contador_de_ninos += 1

if contador_de_ninos > 0:
    promedio = suma_de_estaturas / contador_de_ninos
else:
    promedio = 0

print(f"La cantidad de niños que miden menos de 100 cm es de: {menor_a_100}")
print(f"La cantidad de niños que miden entre 100 y 120cm es de: {entre_100_120}")
print(f"La cantidad de niños que miden entre 121 y 130cm es de: {entre_121_130}")
print(f"La cantidad de niños que miden entre 131 y 140cm es de: {entre_131_140}")
print(f"La cantidad de niños que miden más de 140cm es de: {mayor_que_140}")
print(f"El promedio de estatura es de: {promedio:.2f} cm")
