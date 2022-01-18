'''
2.4 Feladat

A program egy listában tároljon öt darab szót, és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.
'''

import random

lista = ["piton","ron","fred","hagrid","lupin"]

r = random.choice(lista)

print(r)

l = []
jo_lista = []
rossz_lista = []

while True:
  betu = input("A szó betűi:")
  if betu == "":
    break
  else:
    l.append(betu)
    if betu in r:
      jo_lista.append(betu)
    else:
      rossz_lista.append(betu)

print(f'Jó tippek: {jo_lista}')
print(f'Rossz tippek: {rossz_lista}')
print("A szó a", r ,"volt")


