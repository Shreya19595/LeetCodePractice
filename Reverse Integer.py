#!/usr/bin/python

'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.
'''

def main():
    num = int(input("Enter a number : "))
    rev = 0
    neg = -0x80000000
    pos = 0x7fffffff

    def revFunc(num):
        nonlocal rev                       # nonlocal works as global variable
        if (num > 0):
            remainder = num % 10
            rev = (rev * 10) + remainder
            num = num // 10                # // for integer devision
            revFunc(num)
        elif (num < 0):
            num = abs(num)
            remainder = num % 10
            rev = (rev * 10) + remainder
            num = num // 10                
            revFunc(num)
        return rev

    if (num >= neg) and (num < 0):
        rev = revFunc(num) * -1
        print(rev)
    elif (num <= pos) and (num >= 0):
        rev = revFunc(num)
        print(rev)
    else:
        return 0

if __name__ == "__main__":
    main()
    
    
