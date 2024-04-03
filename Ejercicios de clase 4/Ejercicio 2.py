'''
Desarrolle un programa que ordene de forma descendente 3 números.
Suponga que los números son diferentes entre sí.
'''

primer_numero = int(input('Por favor ingrese el primer número: '))
segundo_numero = int(input('Por favor ingrese el segundo número: '))
tercer_numero = int(input('Por favor ingrese el tercer número: '))


if primer_numero == segundo_numero or primer_numero == tercer_numero or segundo_numero == tercer_numero:
    print('\n Los números son iguales.')
else:
    if primer_numero > segundo_numero and primer_numero > tercer_numero:
        primero = primer_numero
        if segundo_numero > tercer_numero:
            segundo = segundo_numero
            tercero = tercer_numero
        else:
            segundo = tercer_numero
            tercero = segundo_numero
    elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
        primero = segundo_numero
        if primer_numero > tercer_numero:
            segundo = primer_numero
            tercero = tercer_numero
        else:
            segundo = tercer_numero
            tercero = primer_numero
    else:
        primero = tercer_numero
        if primer_numero > segundo_numero:
            segundo = primer_numero
            tercero = segundo_numero
        else:
            segundo = segundo_numero
            tercero = primer_numero
    print(f'\n El orden de los números de forma descendente es : {primero}, {segundo}, {tercero}')
