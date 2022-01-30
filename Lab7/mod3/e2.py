#!/usr/bin/env python3
'''
Napisz program, który wczytuje liczby podawane przez użytkownika, 
dodaje je do słownika i określa liczbę ich wystąpień 
(liczby stanowią klucze, a liczby ich wystąpień – wartości). 


*W razie podania elementu niebędącego liczbą całkowitą program
*ma wypisać odpowiedni komunikat i 
*kontynuować działanie. 

*Po naciśnięciu klawisza
*<Enter> bez uprzedniego podania wartości program ma 
*wypisać słownik 
*i zakończyć działanie.
'''




def a1():
  slownik = {}
  while True:
    liczba = input("Podaj liczbe lub nacisnij enter: ")
    if len(liczba) == 0:
      print(slownik)
      return 1
    try:
      liczba = int(liczba)
    except:
      print("Koniecznie podaj liczbe całkowitą")
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