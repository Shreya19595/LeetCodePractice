#!/usr/bin/python

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.
'''

def main():
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))

    counter = 0
    x = format(x, '08b')
    y = format(y, '08b')
    
    #Below code would be helpful incase the binary number has more than 8 bits
    if len(x) != len(y):
        if len(x) > len(y):
            a = len(x) - len(y)
            y = ("0" * a) + y
        elif len(y) > len(x):
            a = len(y) - len(x)
            x = ("0" * a) + x

    for n in range(len(x)):
        if x[n] != y[n]:
            counter += 1
    print(counter)

if __name__ == "__main__":
    main()
