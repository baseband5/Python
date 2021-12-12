#!/usr/bin/env python3

def inputData():
  a = int(input("Podaj a (całkowite): "))
  b = int(input("Podaj b (całkowite): "))
  return a,b

def solve(a,b):
  suma=0
  if (a>b):
    return suma
  for j in range(a if a%2 else a+1, b+1,2):
    suma+=j
  return suma

def main():
  x,y = inputData()
  print("Suma = "+str(solve(x,y)))

if __name__ == "__main__":
  main()