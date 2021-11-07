#!/usr/bin/python

'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

def main():
    nums1 = input("Enter number 1: ")
    nums2 = input("Enter number 2: ")
    
    def intNumber(n):
        num = 0
        for x in n:
            k = ord(x) - 48
            if num == 0:
                num = k
            else:
                num = num * 10 + k
        return num
    
    print(str(intNumber(num1) * intNumber(num2)))

if __name__ == "__main__":
    main()
