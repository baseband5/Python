#!/usr/bin/env python3
import turtle




def drawStar(t,l):
    for i in range(5):
        t.forward(l)
        t.right(360/2.5)


def a1(t):
  drawStar(t,100)
  turtle.done()


def main():
  scr = turtle.Screen()
  tur = turtle.Turtle()
  a1(tur)


def done():
  return True

if __name__ == "__main__":
  main()