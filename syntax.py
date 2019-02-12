#!/usr/bin/python3

class Egg:
    def __init__(self, kind="fried"):
        self.kind = kind

    def whatkind(self):
        return self.kind

def main():
    a, b = 0, 1
    a, b = b, a
    c = (1, 2, 3, 4, 5)
    d = [1, 2, 3, 4, 5]
    print("This is the syntax file.", type(a), a)
    egg()
    print(c)
    print(d)
    s = "Less than" if a < b else "not less than"
    print(s)
    func(1)
    func()
    func(5)

    freid = Egg()
    scrambled = Egg('scrambled')
    print(freid.whatkind())
    print(scrambled.whatkind())

def egg(): print("egg")

def func(a=7):
    for i in range(a, 10):
        print(i, end=' ')
    print()

if __name__ == "__main__": main()