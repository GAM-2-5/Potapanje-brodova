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

#brojdimenzija = 3
#matrica = 25
#brojbrodova = 3

stupci = ['A','B','C','D','E','F','G','H','I','J']

polja = []

for i in range(brojdimenzija):
  for j in range (brojdimenzija):
    polja.append (stupci[i] + str (j + 1))

#print (polja)

print(" ", end =" ")

for i in range(brojdimenzija): 
    if i == (brojdimenzija - 1):
      print(stupci[i])
    else:
      print(stupci[i], end =" ")

for i in range(brojdimenzija): 
    print(i + 1)

brodovi = []

while len(brodovi) < brojbrodova:
  pozbroda = input('Pozicija broda '+ str (len(brodovi) + 1) + ':')
  if pozbroda in polja:
    if pozbroda in brodovi:
      print ('odabrali ste već to polje')
    else:
      brodovi.append (pozbroda)
  else:
    print ('Kriva oznaka pozicije, molim pokušajte ponovno')







  
