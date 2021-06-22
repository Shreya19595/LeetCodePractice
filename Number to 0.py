#!/usr/bin/python

'''
Given a non-negative integer num, return the number of steps to
reduce it to zero. If the current number is even, you have to divide
it by 2, otherwise, you have to subtract 1 from it.
'''

def main():
    num = int(input("Enter a number : "))
    i = 0
    while num != 0:
        if (num % 2 == 0):
            num = num / 2
        else:
            num = num - 1
        i = i + 1
    print (i)

if __name__ == "__main__":
    main()
