#!/usr/bin/env python3
import turtle

def draw_polygon(t,n,length):
  for i in range(n):
    t.forward(length)
    t.left(360/n)
 
def a1():
  scr = turtle.Screen()
  tur = turtle.Turtle()
  n=20
  for i in range(n):
    draw_polygon(tur,4,100)
    tur.left(360/n)
  turtle.done()

def main():
  a1()


def done():
  return True

if __name__ == "__main__":
  main()