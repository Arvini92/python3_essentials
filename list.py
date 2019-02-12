
def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list[0:5])
    list[:] = range(100)
    print(list[27:42:3])
    for i in list[27:43:3] : print(i)
    list[27:43:3] = (99, 99, 99, 99, 99, 99)
    print(list)
    
if __name__ == "__main__": main()