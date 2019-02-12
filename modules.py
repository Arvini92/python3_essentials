#!/usr/bin/python3

import sys

__version__ = "1.1.0"

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))

    import urllib.request
    page = urllib.request.urlopen('http://google.com')
    # for line in page: print(str(line, encoding = 'utf_8'), end = '')

    import random
    print(random.randint(1, 1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

    import datetime
    now = datetime.datetime.now()
    print(now)

    print(now.year, now.month, now.minute, now.second, now.microsecond)

    # import bitstring

    # a = bitstring.BitString(bin = '01010101')
    # print(a.hex, a.bin, a.uint)

        

if __name__ == "__main__": main()