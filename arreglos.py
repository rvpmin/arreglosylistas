#!/usr/bin/env python3
#by rvpmin
#Licence GNU/GPL
#2023/10/30		

#Posiciones especificas
lista = [12,34,56,78,90]
print(lista[3]) #cuarto elemento
print(lista[-3]) #antepenultimo
print(lista[len(lista)-3])  #antepenultimo

#Slices
print(lista[:3]) #primeros 2
print(lista[-5:]) #ultimos 5
print(lista[::2]) #impares

import math
suma = 0
for x in lista:
    suma += x

promedio = suma / len(lista)

desv = 0

for i in lista:
    desv += (i - promedio)**2

desv = math.sqrt((desv / len(lista))
