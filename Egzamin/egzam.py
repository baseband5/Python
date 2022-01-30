#!/usr/bin/env python3
'''OŚWIADCZAM, ŻE ZADANIA EGZAMINACYJNE ROZWIĄZAŁEM SAMODZIELNIE.'''





import random

def F1(L):
  podwojonaWartoscPrzeciwnych=0
  licznik=0
  dlListy = len(L)
  while licznik < dlListy:
    #print(L[licznik])
    if(L[licznik] % 3 == 0 and L[licznik] %5 !=0 ):
      podwojonaWartoscPrzeciwnych-= 2 * L[licznik]
    licznik+=1
  return podwojonaWartoscPrzeciwnych

def F2(L):
  listaDoZwrotu = []
  maleLitery=[]
  duzeLitery=[]
  cyfry=[]
  pozostale=[]
  for znak in L:
    if(znak.islower()):
      maleLitery.append(znak)
    elif(znak.isupper()):
      duzeLitery.append(znak)
    elif(znak.isdigit()):
      cyfry.append(znak)
    else:
      pozostale.append(znak)
  listaDoZwrotu = maleLitery + duzeLitery + cyfry + pozostale
  return listaDoZwrotu

def f3():
  slownik = {}
  wiersz='''To nie ognik. To przewodnik.
Taki drut, a w drucie PRĄD.
Robisz pstryk i włączasz PRĄD!
Elektryczny bystry PRRRRĄD!
I stąd światło?
Właśnie stąd!'''
  plik = open("wiersz.txt", "w")
  plik.write(wiersz)
  plik.flush()
  plik.close()

  nazwapliku = input("Podaj nazwe pliku z wierszem: ")
  try:
    plik = open(nazwapliku, "r")
  except:
    print("problem z otwarciem pliku")
    return 1
  trescpliku = plik.read()
  for litera in trescpliku:
    if(not litera.islower() and not litera.isupper()):
      slownik[litera] = slownik.get(litera, 0) + 1
  plik.close()
  print(slownik)
  return

def f4():
  slownik = {}
  nazwaPliku = input("Podaj Nazwe Pliku: ")
  try:
    plik = open(nazwaPliku, "r")
  except:
    print("Problem z otwarciem pliku")
    return 1
  nrLinii=1
  for linia in plik:
    slownik[nrLinii] = len(linia)
    nrLinii+=1
  plik.close()
  maxLinia=0
  for klucz in slownik:
    if(slownik[klucz] > maxLinia):
      maxLinia = slownik[klucz]
      nrLinii = klucz
  print(nrLinii)
  return

def main():
  print("Zad.1")
  while True:
    lista = [random.randint(-50,50) for i in range(100)]
    print(lista)
    wart = F1(lista)
    print(wart)
    if (wart < 0):
      break

  print("Zad.2")
  lancuchZnakow = input("Podaj lancuch: ")
  if(len(lancuchZnakow) == 0):
    print("Pusty łańcuch")
    return
  print(F2(lancuchZnakow))
  
  print("Zad.3")
  f3()
  
  print("Zad.4")
  f4()
  return


if __name__ == "__main__":
  main()