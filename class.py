
#!/usr/bin/python3

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 argiments, got {}'.format(numargs))
    
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

class Animal:
    def talk(self): print("I have something to say!")
    def walk(self): print("Hey! I am walkin here!")
    def clothes(self): print("I have nice clothes")

class Duck(Animal):
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print("Quack!")

    def walk(self):
        super().walk()
        print("Walks like a duck.")

    def set_color(self, color):
        self.variables['color'] = color

    def get_color(self):
        return self.variables.get('color', None)

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)

def main():
    donald = Duck()
    donald._color = 'blue'
    print(donald._color)
    print(donald.get_variable('color'))
    donald.walk()

    o = inclusive_range(5, 25, 7)
    for i in o: print(i, end = ' ')
   

if __name__ == "__main__": main()