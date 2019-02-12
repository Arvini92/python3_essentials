#!/usr/bin/python3

def main():
    a,b = 0, 1
    while b < 50:
        print(b)
        a, b = b, a + b
    print("Done.")

    for index, line in enumerate('string'):
        if line == 's': print('index {} is an s'.format(index))
    else:
        print('else')
        

if __name__ == "__main__": main()