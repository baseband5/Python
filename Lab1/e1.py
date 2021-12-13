#!/usr/bin/env python3

def a1():
  print(31+30+29)

def a2():
  sum=0
  for x in range(1,11):
    sum+=x
  print(str(sum))

def a3():
  mul=1
  for x in range(1,11):
    mul*=x
  print(str(mul))

def a4():
  years=3
  rate=0.06
  initAmount=1000
  balance=initAmount
  for i in range(0,years+1):
    print("\t After year: "+ str(i) +" Balance: "+str(round(balance,2)))
    balance += balance*rate

def a5():
  logo ="""\t+------+
  \t|Python|
  \t+------+"""
  print(logo)

def main():
  print("1) Leap year: ",end='')
  a1()
  print("2) Addition: ",end='')
  a2()
  print("3) Multiplication: ",end='')
  a3()
  print("4) Balance")
  a4()
  print("5) LOGO ")
  a5()

if __name__ == "__main__":
  main()
