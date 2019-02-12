def b(n): print('{:08b}'.format(n))

def main():
  x, y = 0x55, 0xaa

  b(x)
  b(y)

  b(x | y)
  b(x & y)
  b(x ^ y)
  b(x ^ 0)
  b(x ^ 0xff)
  b(x << 4)
  b(x >> 4)
  b(~x)

  print(x is not y)
  print(True and False)
  print(True or False)

if __name__ == "__main__": main()