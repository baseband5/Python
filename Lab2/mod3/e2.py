#!/usr/bin/env python3
import turtle

def drawRect(t,a,x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  for i in range (4):
    t.forward(a)
    t.left(90)
  t.penup()
  return


def a1():
  tur = turtle.Turtle()
  for i in range (5):
    drawRect(tur,10*(i+1),-5*i,-5*i)
  turtle.done()
  return
  

def main():
  a1()
  return

def done():
  return True

if __name__ == "__main__":
  main()