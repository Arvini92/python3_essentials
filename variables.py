#!/usr/bin/python3

def main():
   x = 42
   y = 42 / 9
   z = 42 // 9
   k = 42 % 9
   num = round(42 / 9, 2)
   print(id(x))
   print(type(x))
   print(type(y), y, num)
   print(z)
   print(k)
   s = 'This is a\n  {}string!'.format(x)
   s = 'This is a\n  %s string!' % x
   s = '''\
   this is a string 
   line after line
   '''    
   print(s)
   print(divmod(5, 3))

if __name__ == "__main__": main()