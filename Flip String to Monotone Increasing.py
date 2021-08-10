#!/usr/bin/python

'''
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.
'''

def main():
    s = list(map(int, input("Enter array: ").strip().split()))
    flip1 = 0
    flip0 = 0

    for i in range(len(s)):
        if s[i] == 0:
            flip1 += 1

        elif s[i] == 1:
            flip1 = min(flip1, flip0)
            flip0 += 1

    print(min(flip1, flip0))

if __name__ == "__main__":
    main()
