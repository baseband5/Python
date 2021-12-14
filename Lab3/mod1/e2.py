#!/usr/bin/env python3

def remove(napis, usuwany):
  #return napis[napis.find(usuwany)+len(usuwany) if napis.find(usuwany) != -1 else 0 :]  
  return napis.replace(usuwany,"",1)

def main():
  stri = "abrakadabra"
  sub = "ab"
  print("2) \""+stri+"\" - \""+sub+"\" = \""+remove(stri,sub)+"\"")

def done():
  return True

if __name__ == "__main__":
  main()