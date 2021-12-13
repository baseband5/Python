#!/usr/bin/env python3

def a1():
  n = int(input("N: "))  
  try:
      assert n>0
  except:
      print ("n<0")
      return
  inita=float(input("a1: "))  
  for i in range (2,n+1):
    a=float(input("a"+str(i)+": "))
    print(a)
  print(inita)

def main():
  print("a) Helper var")
  a1()

def done():
  return True

if __name__ == "__main__":
  main()