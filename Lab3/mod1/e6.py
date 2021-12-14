#!/usr/bin/env python3

def mirror(napis):
  return napis + napis[::-1]

def main():
  stri = "Test"
  print("6) \""+stri+"\" = \""+ str(mirror(stri))+"\"")

def done():
  return True

if __name__ == "__main__":
  main()