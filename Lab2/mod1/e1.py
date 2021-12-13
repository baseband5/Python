#!/usr/bin/env python3
import math

def a1():
  sum=0
  for j in range(2,100+1,2):
    sum+=j
  print("Sum = "+str(sum))

def a2():
  sum=1
  for j in range(1,100+1):
    sum+=math.pow(j,2)
  print("Sum = "+str(sum))

def a3():
  sum=1
  for j in range(1,63+1):
    sum+=math.pow(2,j)
  print("Sum = "+str(sum))

def a4():
  a = int(input("From (int): "))
  b = int(input("To (int): "))
  sum=0
  if (a>b):
    return sum
  for j in range(a if a%2 else a+1, b+1,2):
    sum+=j
  print("Sum = "+str(sum))

def main():
  print("a) Sum of evens")
  a1()
  print("b) Sum of squares")
  a2()
  print("c) Sum of powers")
  a3()
  print("d) Sum of odds")
  a4()

def done():
  return True

if __name__ == "__main__":
  main()