import math
import numpy
import random
notas = random.sample(range(0,100),25)
print(notas)
media = sum(notas)/25
print (f"La media de las notas es {media}")
desviacion_estandar = (((sum(notas - media)) ** 2) / 25) ** (1/2) 
print (f"La desviación estandar es {desviacion_estandar}")
