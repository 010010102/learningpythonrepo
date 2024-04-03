'''
Desarrolle un programa que le indique si su año de nacimiento es en
año bisiesto.

Considere que un año bisiesto es aquel que es divisible entre 4 pero
que no es divisible entre 100, excepto el que es divisible entre 400.
'''

nacimiento = int(input('Vamos a definir si u año de nacimiento es bisiesto o no. Para esto, por favor ingrese su año de nacimiento: '))

if (nacimiento % 4 == 0 and nacimiento % 100 != 0) or nacimiento % 400 == 0:
    print(f"\n De acuerdo a su año de nacimiento ({nacimiento}), el año es bisiesto.")
else:
    print(f"\n De acuerdo a su año de nacimiento ({nacimiento}), el año no es bisiesto.")
