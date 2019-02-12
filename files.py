#!/usr/bin/python3

def main():
    buffersize = 50000
    infile = open('quick/lines.txt')
    outfile = open('new.txt', 'w')
    for line in infile.readlines():
        print(line, file = outfile, end='')
    print('Done.')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print('Done.')

    infile = open('olives.jpg', 'rb')
    outfile = open('new.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print('Done.')

if __name__ == "__main__": main()