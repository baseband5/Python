#!/usr/bin/env python3
import turtle




def drawRegular(n,length):
  scr = turtle.Screen()
  tur = turtle.Turtle()
  for i in range(n):
      tur.forward(length)
      tur.left(360/n)
  turtle.done()


def a1():
  drawRegular(8,100)

def a2():
  drawRegular(9,100)

def a3():
  drawRegular(10,100)

def a4():
  drawRegular(12,100)

def a5():
  drawRegular(15,100)

def a6():
  drawRegular(18,100)

def a7():
  drawRegular(20,100)


def main():
  print("Use direct function a1 to a7 for other examples")
  a1()


def done():
  return True

if __name__ == "__main__":
  main()