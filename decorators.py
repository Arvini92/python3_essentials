
#!/usr/bin/python3

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

    @property
    def color(self):
        return self.variables.get('color', None)

    @color.setter
    def color(self, c):
        self.variables['color'] = c

    @color.deleter
    def color(self, c):
        del self.variables['color']

def main():
    donald = Duck()
    donald._color = 'blue'
    print(donald._color)
    print(donald.get_variable('color'))
    donald.walk()
    donald.color = 'blue'
   

if __name__ == "__main__": main()