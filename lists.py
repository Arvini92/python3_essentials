#!/usr/bin/python3

def main():
   x = (1, 2, 3)
   y = [1, 2, 3]
   y.append(5)
   y.insert(2, 7)
   z = 'string'
   print(type(x), x)
   print(type(z), z[2:4])
   for i in x:
      print(i)

if __name__ == "__main__": main()