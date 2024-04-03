'''
Desarrolle un programa que solicite la distancia
de su casa a la Universidad, el costo por
kilómetro, la cantidad de días a la semana que
viaja a la Universidad y que calcule el costo total
de trasladarse por cuatrimestre.
Asuma que cada visite implica ida y vuelta y
que el cuatrimestre tiene 15 semanas.
'''
import time

distancia = float(input("Por favor ingrese la distancia (km) entre su casa y la universidad: "))
costo_km = float(input("¿Cuál es el costo por kilómetro? "))
dias = int(input("¿Cuántos días va a la universidad por semana? "))

distancia_por_dia = distancia * 2 #Ida y vuelta
distancia_por_semana = distancia_por_dia * dias
distancia_por_cuatrimestre = distancia_por_semana * 15
costo_por_km = distancia * costo_km
costo_por_dia = costo_por_km * 2
costo_por_semana = (costo_por_km * 2) * dias
costo_por_cuatrimestre = costo_por_semana * 15

print("\nGracias por la información.\n")

time.sleep(2) #Agregue este delay para simular proceso de información

print("Si la distancia recorrida entre su casa y la universidad es " + str(distancia) \
      + " km, usted recorre " + str(distancia_por_dia) + " kms por día (ida y regreso)." \
      + "Debido a esto, semanalmente usted recorre en total " + str(distancia_por_semana) + " kms.\n" \
      + "Es decir que en el cuatrimestre habrá recorrido " + str(distancia_por_cuatrimestre) + " kms.\n")

time.sleep(5) #Agregue este delay para dar tiempo de lectura entre párrafos

print("En términos de costos, el costo de ida a la universidad desde su casa es de " + str(costo_por_km) \
      + ", lo cual significa que por día usted gasta " + str(costo_por_dia) + " (ida y vuelta).\n" \
      + "Es decir que por semana usted gasta " + str(costo_por_semana) + ", y la proyección total del" \
      " costo total de su transporte en este cuatrimestre es de " + str(costo_por_cuatrimestre) + ".")
