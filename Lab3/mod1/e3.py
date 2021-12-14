#!/usr/bin/env python3

def remove_all(napis, usuwany):
  return napis.replace(usuwany,"")

def main():
  stri = "abrakadabra"
  sub = "ab"
  print("3) \""+stri+"\" - \""+sub+"\" = \""+remove_all(stri,sub)+"\"")

def done():
  return True

if __name__ == "__main__":
  main()