#!/usr/bin/env python3

def ad():
  a = int(input("From (int): "))
  b = int(input("To (int): "))
  sum=0
  if (a>b):
    return sum
  for j in range(a if a%2 else a+1, b+1,2):
    sum+=j
  print("Sum = "+str(sum))

def main():
  print("d) Sum of odds")
  ad()

if __name__ == "__main__":
  main()