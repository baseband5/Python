'''
Napisz program, 
który wczytuje plik tekstowy linia po linii 
i zapisuje przeczytane linie w pliku wyjściowym poprzedzając je numerem linii. 
Nazwy plików należy zapytać użytkownika programu na początku programu.
'''
#!/usr/bin/env python3

def a1():
  nazwaPlikuOd = input("Podaj nazwe pliku wej:")
  try:
    plik = open(nazwaPlikuOd, 'r')
    linia = plik.readlines()
    plik.close()
  except:
    print ("Coś jest nie tak z plikiem wejściowym")
    return 1
  nazwaPlikuDo = input("Podaj nazwe pliku wyj:")
  try:
    plik = open(nazwaPlikuDo, 'w')
    print(list(enumerate(linia)))
    wyjscie = list(enumerate(linia))
    liniaWyjsciowa = ""
    for krotka in wyjscie:
      liniaWyjsciowa = str(krotka[0]) + ": " + krotka[1]
      plik.write(liniaWyjsciowa)
    plik.close()
  except:
    print ("Coś jest nie tak z plikiem wyjściowym")
    return 1

  return 
  
def main():
  a1()
  


def done():
  return False

if __name__ == "__main__":
  main()