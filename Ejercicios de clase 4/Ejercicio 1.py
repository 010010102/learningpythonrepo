'''
Desarrolle un programa que muestre el mayor de dos números.
Suponga que los números son diferentes entre sí. 
Modifique el programa para que funcione para 4 números.
'''

print('\n En el siguiente programa usted podrá ver cuál es el número mayor.')
print('\n Por favor seleccione cuántos números desea utilizar')
print('\t 2')
print('\t 4')

numeros_utilizados = int(input('\n ¿Cuántos números desea utilizar? '))

if numeros_utilizados == 2:
    primer_numero = int(input('Por favor ingrese el primer número: '))
    segundo_numero = int(input('Por favor ingrese el segundo número: '))
    if primer_numero > segundo_numero:
        print(f'El mayor de los dos números es: {primer_numero}')
    elif primer_numero == segundo_numero:
        print('Ambos números son iguales')
    else:
        print(f'El mayor de los dos números es: {segundo_numero}')
elif numeros_utilizados == 4:
    primer_numero = int(input('Por favor ingrese el primer número: '))
    segundo_numero = int(input('Por favor ingrese el segundo número: '))
    tercer_numero = int(input('Por favor ingrese el tercer número: '))
    cuarto_numero = int(input('Por favor ingrese el cuarto número: '))

    if primer_numero == segundo_numero == tercer_numero == cuarto_numero:
        print('Todos los números son iguales.')
    else:
        numero_mayor = primer_numero
        if segundo_numero > numero_mayor:
            numero_mayor = segundo_numero
        elif tercer_numero > numero_mayor:
            numero_mayor = tercer_numero
        elif cuarto_numero > numero_mayor:
            numero_mayor = cuarto_numero
        print(f'El mayor de los cuatro números es: {mayor_numero}')
else:
    print('Debido a que ha seleccionado una opción que no está disponible, \n'
          'este programa ha finalizado')
