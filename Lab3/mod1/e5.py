#!/usr/bin/env python3

def palindrom(napis):
  return napis.lower() == napis[::-1].lower()

def main():
  stri = "kajak"
  print("5) \""+stri+"\" = \""+ str(palindrom(stri))+"\"")

def done():
  return True

if __name__ == "__main__":
  main()