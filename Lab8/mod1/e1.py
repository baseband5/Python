#!/usr/bin/env python3

def a1():
  plik = open('hello.txt', 'w')
  plik.write("""He he he
      l
lo, World
!""")
  plik.write("\n********")
  #plik.flush()
  plik.close()
  plik = open('hello.txt', 'r')
  linia = plik.readlines()
  plik.close()
  print(linia)
  return 
  
def main():
  a1()
  


def done():
  return False

if __name__ == "__main__":
  main()