#!/usr/bin/env python3

def a1():
  n = float(input("Dzielna: "))
  b = float(input("Dzielnik: "))
  if b!=0:
    print(n/b)
    return
  print("Dzielnik nie może być zerem")
  
def main():
  print("a) excersize")
  a1()

def done():
  return False

if __name__ == "__main__":
  main()