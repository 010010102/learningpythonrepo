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

estaturas = []
cantidad_estaturas = 0

print("Por favor ingrese las estaturas de los niños en centímetros o escriba la palabra 'salir' para terminar):")
while True:
    entrada = input("Digíte la estatura del niño (cm) o 'salir' para terminar: ")
    if entrada.lower() == 'salir':
        break
    try:
        estatura = int(entrada)
        if estatura >= 0:
            estaturas.append(estatura)
            cantidad_estaturas = cantidad_estaturas + 1
        else:
            print("Por favor, ingrese una estatura válida (valor positivo).")
    except ValueError:
        print("Por favor, ingrese una estatura válida (número entero).")

menor_a_100 = 0
entre_100_120 = 0
entre_121_130 = 0
entre_131_140 = 0
mayor_que_140 = 0
total_estaturas = 0

for estatura in estaturas:
    total_estaturas += estatura
    if estatura < 100:
        menor_a_100 += 1
    elif 100 <= estatura <= 120:
        entre_100_120 += 1
    elif 121 <= estatura <= 130:
        entre_121_130 += 1
    elif 131 <= estatura <= 140:
        entre_130_140 += 1
    else:
        mayor_que_140 += 1

if cantidad_estaturas > 0:
    promedio_estaturas = total_estaturas / cantidad_estaturas
else:
    promedio_estaturas = 0

print("\nSegún las estaturas definidas para todos los niños, los resultados son los siguientes:")
print(f"Cantidad de niños que miden menos de 100 cm: {menor_a_100} cm.")
print(f"Cantidad de niños que miden entre 100 y 120 cm: {entre_100_120} cm.")
print(f"Cantidad de niños que miden entre 121 y 130 cm: {entre_121_130} cm.")
print(f"Cantidad de niños que miden entre 131 y 140 cm: {entre_131_140} cm.")
print(f"Cantidad de niños que miden más de 140 cm: {mayor_que_140} cm.")
print(f"El promedio de estatura de todos los niños es de: {promedio_estaturas} cm.")
