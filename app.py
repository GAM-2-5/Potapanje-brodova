import random


brojdimenzija = 0

print('Dozvoljena dimenzija mora biti veća od  0 i manja ili jednaka 9')

while True:
  brojdimenzija = int(input('Broj dimenzija: '))
  if (brojdimenzija > 0 and brojdimenzija <= 9) :
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

stupci = ['A','B','C','D','E','F','G','H','I','J']

polja = []

for i in range(brojdimenzija):
  for j in range (brojdimenzija):
    polja.append (stupci[i] + str (j + 1))

#print (polja)




brodovi = []

brodovi_kompjutora = []

moji_potezi = []

potezi_komp = []

broj_mojih_pogodaka = 0
broj_komp_pogodaka = 0


def print_matrica():
  print(' ') #novi red
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
        if cell in potezi_komp:
          p = 'X'
        else:
          p = 'O'
      else:
        if cell in potezi_komp:
          p = '.'
        
      
      print(p, end =" ")

    print(" ", end =" ")  
    print(i + 1, end =" ") 

    for j in range (brojdimenzija):
      cell = stupci [j] + str(i + 1)
      p = ' '
      if cell in moji_potezi:
        if cell in brodovi_kompjutora:
          p = 'X'
        else:
          p = '.'
      if j == (brojdimenzija - 1):
        print(p)
      else:
        print(p, end =" ")
        
  print(' ') #novi red

print_matrica()



while len(brodovi) < brojbrodova:
  pozbroda = input('Pozicija broda '+ str (len(brodovi) + 1) + ':')
  pozbroda = pozbroda.upper()
  if pozbroda in polja:
    if pozbroda in brodovi:
      print ('odabrali ste već to polje')
    else:
      brodovi.append (pozbroda)
      print_matrica()
      if len(brodovi) == brojbrodova:
        print('Igra pocinje')
  else:
    print ('Kriva oznaka pozicije, molim pokušajte ponovno')


def random_odabir(iz_matrice, u_listu):
  while True:
    r = random.choice(iz_matrice)
    if r not in u_listu:
      u_listu.append(r)
      break



def potez_komjutora():
  #postavljanje varijable broj_komp_pogodaka na globalnu, da je mozemo mijenjati unutar funkcije
  global broj_komp_pogodaka
  
  #kompjutor bira random poziciju iz liste 'polja' i dodaje u listu 'potezi_komp'
  random_odabir(polja, potezi_komp)

  #print('svi potezi kompa: ' + str(potezi_komp))
  #potez nam postaje zadnji element liste
  potez = potezi_komp[len(potezi_komp)-1]

  #printamo potez kompa
  print ('Kompjutor bira potez: ' + str(potez), end =" ")

  #provjeravamo da li je potez kompa u nasim brodovima
  if potez in brodovi:
    broj_komp_pogodaka = broj_komp_pogodaka + 1
    potezi_komp.append(potez)
    print ('... i pogađa !!!! ..bkhkhhkbkhbkh .. ')  
    if broj_komp_pogodaka == len (brodovi):
      print('Zao mi je, izgubili ste ovu partiju')
      print_matrica()

  else: #ako nije potez kompa u nasim brodovima onda printamo missed shot
    print ('.. i promašuje...')

for i in range(brojbrodova):
  random_odabir(polja, brodovi_kompjutora)
    
#print(brodovi_kompjutora)
#brodovi_kompjutora
  

while True:
  pokusaj = input('Potopi brod na poziciji:')
  pokusaj = pokusaj.upper()
  if pokusaj not in polja:
    print ('Kriva oznaka pozicije, molim pokušajte ponovno')
  else:
    if pokusaj in moji_potezi:
      print('Vec ste potapali to polje, molim pokusajte ponovo')
    else:
      moji_potezi.append(pokusaj)
      if pokusaj in brodovi_kompjutora:
        broj_mojih_pogodaka = broj_mojih_pogodaka + 1
        print ('!!! Pogodak ... bkhkhhkbkhbkh !!!')

        if broj_mojih_pogodaka == len (brodovi_kompjutora):
          print('!!! Čestitam, pobjedili ste !!!')
          print_matrica()
          break;
      else:
        print ('missed shot..')

      potez_komjutora()

  print_matrica()
  
