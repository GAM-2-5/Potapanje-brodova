brojdimenzija = int(input('Dimenzija igre: '))
brojbrodova = int(input('Broj brodova: '))
matrica = brojdimenzija*brojdimenzija


while matrica < brojbrodova or brojbrodova <= 0 :
  print(' Broj brodova mora biti veći od  0 i manji od ' + str(matrica))
  brojbrodova = int(input(' Broj brodova: '))
print ('Okej')

