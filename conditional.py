#!/usr/bin/python3

def main():
    v = 'one'
    if v == 'one':
        print('v is one')
    elif v == 'two':
        print('v is two')
    elif v == 'three':
        print('v is three')
    else:
        print('v is some other thing')

    choices = dict(
        one = 'one',
        two = 'two',
        three = 'three',
        fourth = 'fourth',
        fifth = 'fifth'
    )
    print(choices[v])
    print(choices.get(v, 'other'))

if __name__ == "__main__": main()