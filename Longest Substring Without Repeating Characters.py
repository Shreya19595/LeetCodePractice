#!/usr/bin/python

'''
Given a string s, find the length of the longest substring without repeating characters.
'''

import string

def main():
    s = input("Enter the String: ")
    l = 0
    a = []
    for i in range(len(s)):
        if s[i] not in a:
            a.append(s[i])
            l = max(len(a), l)
        else:
            a = a[a.index(s[i])+1:] + [s[i]]
            l = max(len(a), l)
    print(l)

if __name__ == "__main__":
    main()
