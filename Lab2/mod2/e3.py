import turtle



def drawHand(tur,radius,dist,delta,ang):
  tur.penup()
  tur.left(ang)
  tur.forward(radius-dist)
  tur.pendown()
  tur.forward(dist)
  tur.penup()
  tur.forward(delta)
  return

def a1():
  clock=[None]*13
  scr = turtle.Screen()
  scr.setup(500,500)
  scr.bgcolor("#90EE90")

  for i in range(13):
    clock[i]=turtle.Turtle()
    clock[i].shape("turtle")
    clock[i].pencolor("#0000ff")
    if i==12:
      break
    drawHand(clock[i],50,4,15,360/12*i)
    turtle.done()

def main():
  a1()

def done():
  return True

if __name__ == "__main__":
  main()