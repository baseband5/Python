#!/usr/bin/env python3

def a1():
  x="Hello World"
  print(len(x))
  
def a2():
  x="Hello World"
  print(x[0])

def a3():
  x="Hello World"
  print(x[2:5])

def a4():
  x=" Hello World "
  print(x.strip())

def a5():
  x="Hello World"
  print(x.upper())

def a6():
  x="Hello World"
  print(x.lower())

def a7():
  x="Hello World"
  print(x.replace('H','J'))

def a8():
  age = 36
  txt = "My name is John, and I am {}"
  print(txt.format(age))

def main():
  print("1) len()")
  a1()
  print("2) x[0]")
  a2()
  print("3) x[2:5]")
  a3()
  print("4) strip()")
  a4()
  print("5) upper()")
  a5()
  print("6) lower()")
  a6()
  print("7) replace('H','J')")
  a7()
  print("8) format()")
  a8()

def done():
  return True

if __name__ == "__main__":
  main()