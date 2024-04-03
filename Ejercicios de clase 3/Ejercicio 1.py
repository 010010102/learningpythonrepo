'''
Elaborar un programa que muestre un mensaje de bienvenida
para una persona.
Debe imprimir la información como se muestra a continuación:
Bienvenido, estimado Nombre PrimerApellido SegundoApellido. 
'''

primer_nombre = input("Por favor escriba su primer nombre: ")
primer_apellido = input("Por favor escriba su primer apellido: ")
segundo_apellido = input("Por favor escriba su segundo apellido: ")

print(f"Bienvenido, estimado {primer_nombre} {primer_apellido} {segundo_apellido}")
