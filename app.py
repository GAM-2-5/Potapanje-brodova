'''
brojdimenzija = 0

print('Dozvoljena dimenzija mora biti veća od  0 i manja ili jednaka 10')

while True:
  brojdimenzija = int(input('Broj dimenzija: '))
  if (brojdimenzija > 0 and brojdimenzija <= 10) :
    matrica = brojdimenzija*brojdimenzija
    print ('Igra ce se igrati na matrici ' + str(brojdimenzija) + 'x' + str(brojdimenzija))
    break
  else : 
    print('Unijeli ste krivu dimenziju, molim vas pokušajte ponovno') 



print("")
brojbrodova = 0


print('Dozvoljen broj brodova je ' + str(matrica))

while True:
  brojbrodova = int(input('Broj brodova: '))
  if (brojbrodova > 0 and brojbrodova <= matrica) :
    print ('Izabrali ste ' + str(brojbrodova) + ' brodova.')
    break
  else : 
    print('Unijeli ste krivi broj brodova, molim vas pokušajte ponovno')


print("")
'''
brojdimenzija = 5
matrica = 25
brojbrodova = 3

stupci = ['A','B','C','D','E','F','G','H','I','J']

polja = []

for i in range(brojdimenzija):
  for j in range (brojdimenzija):
    polja.append (stupci[i] + str (j + 1))

#print (polja)




brodovi = []

brodovi_kompjutora = ['B2', 'C4']

moji_potezi = []

potezi_komputora = []




def print_matrica():
  print(" ", end =" ")

  #printamo slova od nase matrice

  for i in range(brojdimenzija): 
      print(stupci[i], end =" ")

  print("   ", end =" ")

  #printamo slova od matrice kompjutora

  for i in range(brojdimenzija): 
    if i == (brojdimenzija - 1):
      print(stupci[i])
    else:
      print(stupci[i], end =" ")

  #printamo brojeve i brodove od naše matrice

  for i in range(brojdimenzija):
    print(i + 1, end =" ") 
    for j in range (brojdimenzija):
      cell = stupci [j] + str(i + 1)
      p = ' '
      if cell in brodovi:
        p = 'O'
      if j == (brojdimenzija - 1):
        print(p)
      else:
        print(p, end =" ")

  #printamo pogađanja kompjutora

  for i in range(brojdimenzija):
    print(i + 1, end =" ") 
    for j in range (brojdimenzija):
      cell = stupci [j] + str(i + 1)
      p = ' '
      if cell in brodovi:
        p = 'O'
      if j == (brojdimenzija - 1):
        print(p)
      else:
        print(p, end =" ")


print_matrica()


'''
while len(brodovi) < brojbrodova:
  pozbroda = input('Pozicija broda '+ str (len(brodovi) + 1) + ':')
  if pozbroda in polja:
    if pozbroda in brodovi:
      print ('odabrali ste već to polje')
    else:
      brodovi.append (pozbroda)
      print_matrica()
  else:
    print ('Kriva oznaka pozicije, molim pokušajte ponovno')
'''
