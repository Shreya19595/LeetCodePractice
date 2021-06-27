#!/usr/bin/python

'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

def main():
    n = int(input("Enter a number : "))

    def recursion(n):
        rem = 0
        total = 0
        while (n != 0):
            rem = n % 10
            n = n // 10
            total += rem**2
        return total

    while True:
        if(recursion(n) == 1):
            print("True")
            return True
        n = recursion(n)
        if (n < 10):
            print("False")
            return False

if __name__ == "__main__":
    main()
