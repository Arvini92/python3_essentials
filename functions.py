#!/usr/bin/python3

def main():
   testfunc(1, 2, 3, one = 1, two = 2, four = 42)

def testfunc(number = None, *args, **kwargs):
    if number is None:
        print('test')
    for n in args: print(n, end=' ')

    print('This is a test function', kwargs['one'], kwargs['two'])
    for n in kwargs: print(n, kwargs[n], end=' ')

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

for n in primes():
    if n > 100: break
    print(n)



if __name__ == "__main__": main()