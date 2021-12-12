#!/usr/bin/env python3

def main():
  a1()
  a2()
  a3()
  a4()
  a5()

if __name__ == "__main__":
  main()


def a1():
  print("1) ",end='')
  print(31+30+29)

def a2():
  sum=0
  for x in range(1,11):
    sum+=x
  print("2) " + str(sum))

def a3():
  mul=1
  for x in range(1,11):
    mul*=x
  print("3) " + str(mul))

def a4():
  years=3
  rate=0.06
  initAmount=1000
  balance=initAmount
  print("4) ",end='')
  for i in range(0,years+1):
    print("\t After year: "+ str(i) +" Balance: "+str(round(balance,2)))
    balance += balance*rate

def a5():
  print("5) ",end='')
  logo ="""\t+------+
  \t|Python|
  \t+------+"""
  print(logo)