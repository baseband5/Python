#!/usr/bin/env python3
'''
Napisz program, 
*który czyta kolejne linie ze standardowego wejścia 
*i rozkłada linie na słowa za pomocą metody split(). 
Następnie dla otrzymanej listy elementów sprawdza, czy kolejny element jest liczbą
jeżeli jest, to dodaje go do słownika. 

*Program kończy wczytywanie po wczytaniu pustej linii. 
*Program ma wypisać słownik,w którym kluczami są liczby, a wartościami – liczby ich wystąpień.
'''

def a1():
  slownik = {}
  while True:
    lancuch = input("Wpisz: ")

    if len(lancuch) == 0:
      print(slownik)
      return 1
    
    slowa = lancuch.split()
    #print(linia)
    for element in slowa:
      try:
        liczba = int(element)
      except:
        continue
      slownik[liczba] = slownik.get(liczba,0) + 1
 
  return 0

  
def main():
  a1()
  return
  


def done():
  return False

if __name__ == "__main__":
  main()