#!/usr/bin/env python3
import turtle




def drawRegular(n,length):
  scr = turtle.Screen()
  tur = turtle.Turtle()
  for i in range(n):
      tur.forward(length)
      tur.left(360/n)
  turtle.done()


def a1(t):
  drawRegular(8,100)

def a2(t):
  drawRegular(9,100)

def a3(t):
  drawRegular(10,100)

def a4(t):
  drawRegular(12,100)

def a5(t):
  drawRegular(15,100)

def a6(t):
  drawRegular(18,100)

def a7(t):
  drawRegular(20,100)


def main():
  print("Use direct function a1 to a7 for other examples")
  a1()


def done():
  return True

if __name__ == "__main__":
  main()