'''
Gestión de Empleados

Según el algoritmo del programa este será el seudocódigo base:

Paso 1. Al abrir el programa se pregunta al usuario si desea ingresar los datos de un empleado.

Paso 2. Si el usuario escribe que no o salir, el programa termina. 

Paso 3. Si el usuario responde sí o entrar, se procede a ingresar el nombre del empleado.

Validaciones: 
- Si el usuario ingresa algo diferente a sí, entrar, no o salir, se le solicitará al usuario que digite una opción válida.
- Si el usuario no ingresa el nombre del empleado, el programa le solicitará al usuario que agregue un nombre para asegurarse de tener todos los datos.

Paso 4. Seleccionar el tipo de moneda de pago.

Validación: Si el usuario escoge una moneda no válida se le solicitará que seleccione una de las dos opciones.

Paso 5. Luego el usuario deberá agregar el número de horas trabajadas en un mes.

Validación: Si el usuario no ingresa el número de horas trabajadas o ingresa un valor igual o menor que cero, el programa le solicitará al usuario que agregue un número de horas (correcto).

Paso 6. Luego el usuario deberá agregar la tarifa por hora.

Validación: Si el usuario no ingresa la tarifa por hora o ingresa un valor igual o menor que cero, el programa le solicitará al usuario que agregue una tarifa por hora (correcta).

Paso 7. Por último el usuario deberá agregar la evaluación de desempeño según los criterios definidos en formato texto.

Validación: Si el usuario no ingresa una evaluación o si la evaluación no es una de las que se muestra en el menú, el programa le solicitará al usuario que escoja uno de los valores listados.


Paso 8. De acuerdo a los valores definidos en el número de horas trabajadas y la tarifa por hora, se calcula el valor del salario.

Paso 9. Luego, basado en el valor ingresado por el usuario como evaluación de desempeño, se calcula el porcentaje del bono. 

Paso 10. Se presentará en pantalla la información del empleado, su salario total, su bono y su salario total con bono incluido.

Paso 11. Una vez que se ha presentado la información procesada se preguntará al usuario si quiere agregar la información de un nuevo empleado y se vuelve al paso 2.

'''

print('Bienvenido al sistema de gestión de empleados \n')

# Declaración de variables por utilizar
salario = 0
moneda = 0
horas_trabajadas = 0
tarifa_por_hora = 0
bono = 0
bono_calculado = 0
salario_neto = 0

# Inicio del programa
while True:
    respuesta = input('¿Desea agregar la información de un empleado?  \n'
                  'Escriba sí o entrar para continuar. Si desea finalizar escriba no o salir: ')
    
    print('\n')         
    
    # Validación de respuesta inicial por parte del usuario. Se presentan dos opciones para continuar
    if respuesta.lower() == 'sí' or respuesta.lower() == 'si' or respuesta.lower() == 'continuar':

        # Agregando el tipo de moneda de pago
        while True:
            moneda = int(input('Por favor seleccione el tipo de moneda en la que se le paga al empleado:  \n'
                                            'Digite 1 para dólares ($). \n'
                                            'Digite 2 para colones (₡). \n \n'
                                            f'¿Qué moneda desea utilizar?: '))

            if moneda == 1:
                moneda = str('$')
                print('Gracias por escoger el tipo de moneda en dólares.')
                print('\n')
                break
            
            elif moneda == 2:
                moneda = str('₡')
                print('Gracias por escoger el tipo de moneda colones.')
                print('\n')
                break
                    
            else:
                print('La opción seleccionada no existe.')


        while True:
            nombre_empleado = input('Por favor ingrese el nombre del empleado: ')            
            if not nombre_empleado:
                print('No ha ingresado un nombre')
            else:
                print('\n')
                break

        # Validación de ingreso de horas para evitar cálculos vacíos
        while True:
            horas_trabajadas = input('Por favor ingrese el total de horas trabajadas en el mes: ')
            if not horas_trabajadas or int(horas_trabajadas) <= 0:
                print('No ha ingresado horas o ha ingresado un valor no permitido (igual o menor que cero)')
            else:
                print('\n')
                break
            
        # Validación de ingreso de tarifa por hora para evitar cálculos vacíos
        while True:
            tarifa_por_hora = input('Por favor ingrese la tarifa por hora trabajada: ')
            if not tarifa_por_hora or int(tarifa_por_hora) <= 0:
                print('No ha ingresado una tarifa o ha ingresado un valor no permitido (igual o menor que cero)')
            else:
                print('\n')
                break

        # Menú de opciones y validación de uso correcto de las opciones
        while True:
            evaluacion_de_desempeno = int(input('Por favor seleccione una de las siguientes opciones para la evaluación de desempeño del empleado:  \n'
                                            'Digite 1 para Excelente. \n'
                                            'Digite 2 para Bueno. \n'
                                            'Digite 3 para Regular. \n \n'
                                            f'¿Qué tal fue el desempeño de {nombre_empleado}?: '))

            if evaluacion_de_desempeno == 1:
                evaluacion_de_desempeno = str('Excelente')
                bono = 0.1
                break
            
            elif evaluacion_de_desempeno == 2:
                evaluacion_de_desempeno = str('Bueno')
                bono = 0.05
                break
            
            elif evaluacion_de_desempeno == 3:
                evaluacion_de_desempeno = str('Regular')
                bono = 0.0
                break
            
            else:
                print('La opción seleccionada no existe.')    

        # Casteo de variables por si acaso
        salario = float(horas_trabajadas) * float(tarifa_por_hora)
        bono_calculado = float(salario) * float(bono)
        salario_neto = float(salario) + (float(salario) * float(bono))
        bono_porcentual = float(bono) * 100
        
        # Presentación de ressultados
        print('\n')
        print('INFORMACIÓN GENERAL')
        print(f'Nombre de empleado: {nombre_empleado}')
        print(f'Horas trabajadas: {horas_trabajadas}')
        print(f'tarifa por hora: {tarifa_por_hora}')
        print(f'Resultado de evaluación: {evaluacion_de_desempeno}')
        print('\n')
        print('RESULTADOS:')
        print(f'Salario bruto: {moneda}{salario}')
        print(f'Bono: {moneda}{bono_calculado} ({bono_porcentual}%)')
        print(f'Salario neto (salario + bono): {moneda}{salario_neto}')
        print('\n')
        
    # Salida del programa en caso de no querer continuar
    elif respuesta.lower() == 'no' or respuesta.lower() == 'salir':
        print('Ha escogido salir del programa. Gracias por usar el sistema de gestión de empleados.')
        break

    # Validación en caso de no escribir correctamente las instrucciones de entrar o salir del programa
    else:
        print('La opción definida no es válida')
        print('\n')  

