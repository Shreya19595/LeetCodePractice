#!/usr/bin/python

'''
Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

def main():
    n = int(input("Enter number: "))
    ans = []

    for num in range(n + 1):
        n = bin(num).replace("0b", "")
        ans.append(n.count('1'))

    print(ans)

if __name__ == "__main__":
    main()
