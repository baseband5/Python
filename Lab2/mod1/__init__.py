#!/usr/bin/env python3
from .e1 import *
from .e2 import *
from .e3 import *
from .e4 import *

def main(debug = False):
  print(__name__ +" : exercise 1:")
  if debug:
    print("Done: " + str(e1.done()))
  else:
    e1.main()
  
  print(__name__ +" : exercise 2:")
  if debug:
    print("Done: " + str(e2.done()))
  else:
    e2.main()

  print(__name__ +" : exercise 3:")
  if debug:
    print("Done: " + str(e3.done()))
  else:
    e2.main()
  
  print(__name__ +" : exercise 4:")
  if debug:
    print("Done: " + str(e4.done()))
  else:
    e2.main()
  
  def done():
    c =( e1.done() and 
    e2.done() and 
    e3.done() and 
    e3.done() and 
    e4.done() )
    return c