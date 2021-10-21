#!/usr/bin/python

'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
'''

def main():
    x = input("Enter number: ")

    x = str(x)
    i = 0
    j = len(x) - 1
    
    while (i <= j):
        if x[i] != x[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

if __name__ == "__main__":
    main()
