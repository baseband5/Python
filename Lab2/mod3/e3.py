#!/usr/bin/env python3
import turtle




def draw_polygon(t,n,length):
  for i in range(n):
      t.forward(length)
      t.left(360/n)
  turtle.done()


def a1():
  scr = turtle.Screen()
  tur = turtle.Turtle
  draw_polygon(tur,8,100)
  turtle.done()

def main():
  a1()


def done():
  return True

if __name__ == "__main__":
  main()