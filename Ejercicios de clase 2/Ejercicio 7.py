'''
Desarrolle un programa que solicite al
usuario la edad de 5 personas y le muestre cuál
es la edad promedio.
'''

edad1 = int(input("Por favor ingrese edad de la primera persona: "))
edad2 = int(input("Por favor ingrese edad de la segunda persona: "))
edad3 = int(input("Por favor ingrese edad de la tercera persona: "))
edad4 = int(input("Por favor ingrese edad de la cuarta persona: "))
edad5 = int(input("Por favor ingrese edad de la quinta persona: "))

promedio = (edad1 + edad2 + edad3 + edad4 + edad5) / 5

print("La edad promedio es: ", promedio)




# Otra forma de hacerlo

edades = 0

for i in range(5):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: ")) #Agregando f-string para formatear el unput
    edades = edades + edad
    
promedio = edades / 5

print(f"La edad promedio es: {promedio}") #Agregando f-string para formatear el print
