#!/usr/bin/env python3
import turtle

def draw_polygon(t,n,length):
  for i in range(n):
    t.forward(length)
    t.left(360/n)
 
def a1():
  scr = turtle.Screen()
  scr.colormode(255)
  tur = turtle.Turtle()
  
  tur.speed(0)
  tur.begin_fill()
  n=20
  for i in range(n):
    tur.begin_fill()
    tur.pencolor(int(255/n*i),int(255/n*i),int(255/n*i))
    tur.fillcolor(int(255-255/n*i),int(255-255/n*i),int(255-255/n*i))
    draw_polygon(tur,6,100)
    tur.left(360/n)
    tur.end_fill()
  turtle.done()

def main():
  a1()


def done():
  return True

if __name__ == "__main__":
  main()