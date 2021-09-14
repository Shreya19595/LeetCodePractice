#!/usr/bin/python

'''
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
'''

import string

def main():
    s = list(input("string:"))
    alpha = [i for i in s if i.isalpha()]
    a = []
    for i in s:
        if i.isalpha():
            a.append(alpha.pop())
        else:
            a.append(i)
    print("".join(a))
    
if __name__ == "__main__":
    main()
