#!/usr/bin/env python3

def a1():
  for a in range(7):
    if(a==3 or a==6):
      continue
    print(str(a))
  return

def a2():
  n = int(input("N: "))
  for a in range(n):
    if(a%3!=0 and a%6 !=0):
      continue
    print(str(a))
  return

def a3():
  lim = float(input("Lim: "))
  sum = 0
  while True:
    sum += float(input("x: "))
    if(sum>lim):
      break
  return

def a4():
  lim = float(input("Lim: "))
  sum = 0
  while True:
    x = float(input("x: "))
    if x<0:
      continue
    sum +=x
    if(sum>lim):
      break
  return


def main():
  a4()

def done():
  return False

if __name__ == "__main__":
  main()