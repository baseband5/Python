#!/usr/bin/env python3
import turtle

def draw_spiral(t,x,y,ang):
    for i in range(70):
        t.forward(5+(2*i))
        t.right(ang)


def a1():
  scr = turtle.Screen(500,500)
  tur = turtle.Turtle()
  draw_spiral(tur,10,10,95)
  turtle.done()

def main():

  a1()


def done():
  return True

if __name__ == "__main__":
  main()