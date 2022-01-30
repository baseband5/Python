#!/usr/bin/env python3
from .e1 import *
from .e3 import *

def main(debug = False):
  print(__name__ +" : exercise 1:")
  if debug:
    print("Done: " + str(e1.done()))
  else:
    e1.main()
  