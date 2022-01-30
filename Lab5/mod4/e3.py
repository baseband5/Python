import random as r
def a1():
  lista = [r.randint(-100,100) for i in range(20)]
  print(lista)
  print(ile_ujemnych(lista))



def a2():
  lista = []
  while len(lista)<10:
    n = int(input("Wczytaj liczbę, którą chcesz dodać do listy: "))
    if(n not in lista): 
      lista.append(n)
  print(lista)
  return

def ile_ujemnych(lista):
  l=0
  for i in lista:
    if(i<0):
      l+=1
  return l

def main():
  a2()

if __name__ == "__main__":
  main()