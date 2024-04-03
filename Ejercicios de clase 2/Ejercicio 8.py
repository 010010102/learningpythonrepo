'''
Desarrolle un programa que solicite al usuario la
cantidad de horas semanales trabajadas, el
precio que se le paga por hora y que calcule el
salario mensual.
Considere que se debe aplicar una deducción
del 10.5% por cargas sociales y 5% por
asociación solidarista.
Asuma que cada mes cuenta con 4.2 semanas.
'''

horas_trabajadas = float(input("Por favor ingrese la cantidad de horas que trabaja por semana: "))
pago_por_hora = float(input("Por favor confirme cuánto gana por hora: "))

pago_por_semana = horas_trabajadas * pago_por_hora
salario_mensual = pago_por_semana * 4.2 
carga_social = salario_mensual * 0.105
asociacion_solidarista = salario_mensual * 0.05
total_deducciones = carga_social + asociacion_solidarista
salario_neto = salario_mensual - total_deducciones

print(f"Su salario bruto mensual es de: {salario_mensual} \n" \
      f"De su salario bruto se deducen {total_deducciones}. ({carga_social} en concepto de carga social"\
      f" y {asociacion_solidarista} en concepto de asociación solidarista)\n" \
      f"Es decir que su salario neto es de {salario_neto}.")
