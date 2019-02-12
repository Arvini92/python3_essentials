#!/usr/bin/python3

def main():
    try:
        fh = open('xlines.txt')
        for line in fh.readlines():
            print(line.strip())
    except IOError as e:
        print("something bad happened ({})".format(e))

    print("after badness")

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('File must end with .txt')

if __name__ == "__main__": main()