#!/usr/bin/env python3

import math

def a1():
  n = int(input("N: "))
  ndiv = getDivisors(n)
  ndiv.pop(0)
  ndiv.pop()

  for i in range(2,n):
    idiv = getDivisors(i)
    idiv.pop(0)
    for j in idiv:
      if j in ndiv:
        print (str(i) +" nie jest")
        break
    print (str(i) +" jest")
  return

def a2():
  n = int(input("N: "))
  
  for i in range(1,n):
    if(isPerfect(i)):
      print(str(i) + ": jest doskonałe")
  
  return

def a3():
  n = int(input("N: "))

  for a in range(n):
    for b in range(n):
      for c in range(n):
        if( pow(a,2) + pow(b,2) + pow(c,2) == n):
          print(str(a)+"^2 + "+str(b)+"^2 + "+str(c)+"^2 = "+str(n))
  return



def isPerfect(num):
    divNumWONum = getDivisors(num)
    divNumWONum.pop()
    sumOfDivisors = sum(divNumWONum)
    if (sumOfDivisors == num):
        return True
    else: 
        return False

def getDivisors(x):
    divisors = []
    for i in range(1,x+1):
        if(x%i==0):
            divisors.append(i)
    "test".is
    return divisors
    
def main():
  
  a3()

def done():
  return False

if __name__ == "__main__":
  main()