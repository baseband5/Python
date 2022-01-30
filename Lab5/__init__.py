#!/usr/bin/env python3
#from .mod1 import *
from .mod2 import *
from .mod3 import *
from .mod4 import *

def main(debug = False):
  print(__name__ +" : mod 1:")
  if debug:
    print("Done: " + str(mod1.done()))
  else:
    mod1.main()
  
  print(__name__ +" : mod 2:")
  if debug:
    print("Done: " + str(mod2.done()))
  else:
    mod2.main()

  print(__name__ +" : mod 2:")
  if debug:
    print("Done: " + str(mod3.done()))
  else:
    mod3.main()
  print(__name__ +" : mod 4:")
  if debug:
    print("Done: " + str(mod4.done()))
  else:
    mod4.main()

    
  def done():
    c =( mod1.done() and 
    mod2.done()
    ) 
    return c