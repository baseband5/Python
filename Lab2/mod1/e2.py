#!/usr/bin/env python3
import math


def a1():
  n = int(input("N: "))  
  sum=0
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    sum +=  a 
  print("Sum:", sum)

def a2():
  n = int(input("N: "))  
  mul=1
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    mul *= a
  print("Multiplication:", mul) 

def a3():
  n = int(input("N: "))  
  sum=0
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    sum +=  abs(a) 
  print("Sum:", sum)

def a4():
  n = int(input("N: "))  
  sum=0
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    sum +=  math.sqrt(abs(a)) 
  print("Sum:", sum)

def a5():
  n = int(input("N: "))  
  mul=1
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    mul *=  abs(a) 
  print("Multiplication:", mul)

def a6():
  n = int(input("N: "))  
  sum=0
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    sum += math.pow(a,2) 
  print("Sum:", sum)

def a7():
  n = int(input("N: "))  
  sum=0
  mul=1
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    sum +=  a 
    mul *= a
  print("Sum:", sum)
  print("Multiplication:", mul) 

def a8():
  n = int(input("N: "))  
  sum=0
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    sum += math.pow(-1,i+2) * a  
  print("Sum:", sum)

def a9():
  n = int(input("N: "))  
  sum=0
  for i in range (n):
    a=float(input("a"+str(i+1)+": "))
    sum += math.pow(-1,i+1) * (a/math.factorial(i+1))  
  print("Sum:", sum)

def main():
  print("a) Simple sum")
  a1()
  print("b) Simple multiplication")
  a2()
  print("c) Sum of absolutes")
  a3()
  print("d) Sum of sqrt(abs)")
  a4()
  print("e) Mul of absolutes")
  a5()
  print("f) Sum of squares")
  a6()
  print("g) Sum and mul")
  a7()
  print("h) Alternate sum")
  a8()
  print("i) alternate sum with factorial divider")
  a9()
  return

def done():
  return True

if __name__ == "__main__":
  main()