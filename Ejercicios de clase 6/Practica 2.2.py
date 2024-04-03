'''
Desarrollar un programa que le solicite al usuario
un valor y muestre los primeros 10 números
divisibles entre este valor.
'''

numero_inicial = int(input("Por favor ingrese un valor para encontrar 10 números divisibles por el mismo: "))

contador = 0
numero = 1

print(f"Los primeros 10 números divisibles por {numero_inicial} son:")

while contador < 10:
    if numero % numero_inicial == 0:
        print(numero)
        contador = contador + 1  
    numero = numero + 1  
