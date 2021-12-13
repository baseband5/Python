#!/usr/bin/env python3

import math

def ai():
  n = int(input("N: "))
  sum = 0
  for x in range(n):
    a = float(input("a"+ str(x+1) + ": "))
    sum += ((-1)**(x+1))*(math.factorial(a)/math.factorial(x+1))
  print(str(round(sum,2)))

def main():
  print("i) Alternating factorial sum")
  ai()

if __name__ == "__main__":
  main()