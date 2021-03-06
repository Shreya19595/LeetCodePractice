#!/usr/bin/python

'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 
That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''

def main():
    n = int(input("Enter number: "))
    if n <= 1:
        print(n)
    
    a, b, c = 0, 1, 0
    while n > 1:
        n -= 1
        c = a + b
        a, b = b, c
    print(c)

if __name__ == "__main__":
    main()
