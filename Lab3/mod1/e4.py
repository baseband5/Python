#!/usr/bin/env python3

def reverse(napis):
  return napis[::-1]

def main():
  stri = "abrakadabra"
  print("4) \""+stri+"\" = \""+reverse(stri)+"\"")

def done():
  return True

if __name__ == "__main__":
  main()