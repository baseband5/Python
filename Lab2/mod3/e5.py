#!/usr/bin/env python3
import turtle

def drawStar(t,l):
    t.seth(0)
    for i in range(5):
        t.forward(l)
        t.right(360/2.5)
    t.seth(0)


def a1():
  scr = turtle.Screen(500,500)
  tur = turtle.Turtle()
  for i in range(5):
    drawStar(tur,10)
    tur.penup()
    tur.seth(-144*(i))
    tur.forward(50)
    tur.pendown()
  turtle.done()


def main():

  a1()


def done():
  return True

if __name__ == "__main__":
  main()