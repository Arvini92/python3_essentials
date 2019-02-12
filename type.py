#!/usr/bin/python3

def main():
   x = 42
   y = 42 
   print(x is y)
   k = dict( x = 42)
   z = dict( x = 42)
   print(x == y)
   print(k is z)

if __name__ == "__main__": main()