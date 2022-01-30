#!/usr/bin/env python3

def a1():
  lista =[]
  for i in range(10):
    lista.append(i+1)
  print(str(lista))

  return

def a2():
  lista =[i*2 for i in range(11)]
  print(str(lista))
  return

def a3():
  lista =[i*i for i in range(11)]
  print(str(lista))
  return

def a4():
  lista = [0 for i in range(10)]
  print(str(lista))
  return

def a6():
  lista =[i%5 for i in range(10)]
  print(str(lista))
  return


def main():
  a4()

def done():
  return False

if __name__ == "__main__":
  main()