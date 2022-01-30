#!/usr/bin/env python3

def a1():

  n = int(input("Wpisz liczbę: "))

  il = 1
  while n > 0:
    il *= 2
    n -= 1
  print(il)
  
def main():
  print("a) excersize")
  a1()

def done():
  return False

if __name__ == "__main__":
  main()