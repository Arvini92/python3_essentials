#!/usr/bin/python3
import re

def main():
    fh = open('raven.txt')
    for line in fh:
        pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
        match = re.search(pattern, line)
        if match:
            print(line, end='')
            print(match.group(), end='')
            print(line.replace(match.group(), '###'), end='')
            print(pattern.sub('###', line), end='')
        # print(re.sub('(Len|Neverm)ore', '###', line), end='')


if __name__ == "__main__": main()