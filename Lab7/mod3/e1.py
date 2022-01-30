#!/usr/bin/env python3

def a1(lancuch):
  slownik ={}
  for litera in lancuch:
    slownik[litera] = slownik.get(litera,0) + 1
  return slownik

def a2(lancuch):
  slownik ={}
  for litera in lancuch:
    if litera.isalpha():
      slownik[litera] = slownik.get(litera,0) + 1
  return slownik

def a3(lancuch):
  slownik ={}
  lancuch = lancuch.lower()
  for litera in lancuch:
    if litera.isalpha():
      slownik[litera] = slownik.get(litera,0) + 1
  return slownik

def a4(lancuch):
  slownik = a3(lancuch)
  topZnak=""
  topIlosc=0
  for wartosc in slownik:
    if slownik[wartosc] >= topIlosc:
      topIlosc = slownik[wartosc]
      topZnak = wartosc
  #print(list(slownik.keys()))
  #print(list(slownik.values()))
  #print(list(slownik.items()))
  return topZnak

  
def main():
  print(a4("abrakadddddabra"))
  


def done():
  return False

if __name__ == "__main__":
  main()