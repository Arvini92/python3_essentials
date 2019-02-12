#!/usr/bin/python3

def main():
  s = 'string ti'
  print('string'.upper())
  print('string {}'.format(42))
  print('string %d' % 42)
  print('string'.capitalize())
  print('string'.swapcase())
  print('string'.find('in'))
  print('string'.strip())
  print('string'.rstrip())
  print('string'.isalnum())
  print('string'.isalpha())
  print('first {1} zero {0} first {1}'.format(0, 1))
  print('first {bob} zero {fred}'.format(bob = 0, fred = 1))
  d = dict(bob = 0, fred = 1)
  print('first {bob} zero {fred}'.format(**d))
  print(s.split('i'))
  words = s.split('i')
  new = ":".join(words)
  print(new)
  new = s.center(80)
  print(new)




if __name__ == "__main__": main()