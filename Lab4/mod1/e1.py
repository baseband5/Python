#!/usr/bin/env python3

def a1():
  a = int(input("Podaj a: "))
  if a<0:
    print(-a)
    return
  print(a)
  return

def main():
  print("a) abs")
  a1()

def done():
  return False

if __name__ == "__main__":
  main()