#!/usr/bin/env python3
import math

def a1():
  radius=float(input("Radius: "))
  solve=2*math.pi*radius
  print("Circumference: "+ str(round(solve,2)))

def a2():
  radius=float(input("Radius: "))
  solve=math.pi*math.pow(radius,2)
  print("Area: "+ str(round(solve,2)))

def a3():
  a=float(input("Base: "))
  b=float(input("Top: "))
  h=float(input("Height: "))
  solve=((a+b)*h)/2
  print("Area: "+ str(round(solve,2)))

def a4():
  a=float(input("a: "))
  b=float(input("b: "))
  c=float(input("c: "))
  p=(a+b+c)/2
  if (a + b <= c or a + c <= b or b + c <= a):
    print("Triangle sides not corect!")
    return
  solve=math.sqrt(p*(p-a)*(p-b)*(p-c) )
  print("Area: "+ str(round(solve ,2)))

def a5():
  ang=float(input("Deg: "))
  solve=ang*math.pi/180
  print("Rad: "+ str(round(solve ,2)))
  
def a6():
  ang=float(input("Rad: "))
  solve=ang*180/math.pi
  print("Deg: "+ str(round(solve ,2)))

def main():
  print("1) Circle circumference")
  a1()
  print("2) Circle area")
  a2()
  print("3) Trapeze area")
  a3()
  print("4) Triangle area")
  a4()
  print("5) Deg to Rad")
  a5()
  print("6) Rad to Deg")
  a6()
  return

if __name__ == "__main__":
  main()
