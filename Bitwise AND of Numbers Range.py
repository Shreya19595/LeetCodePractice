#!/usr/bin/python

'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
'''

def main():

    left = int(input("Enter left: "))
    right = int(input("Enter right: "))
    if left == 0 and right == 0:
        print("0")
    elif len(bin(left)) != len(bin(right)):
        print("0")
    else:
        left = bin(left)[2:]
        right = bin(right)[2:]
        for i in range(len(right)):
            if left[i] != right[i]:
                left = left[:i] + ("0" * len(right[i:]))
                break
        print(int(left, 2))

if __name__ == "__main__":
    main()
