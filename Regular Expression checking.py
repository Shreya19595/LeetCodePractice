#!/usr/bin/python

'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

import re

def main():
    s = input("Enter string: ")
    p = input("Enter matching string: ")
    
    if len(re.findall(p,s)) == 0:
        print("Not a match")
    if re.findall(p,s)[0] == s:
        print("It's a match")
    else:
        print("Not a match")

if __name__ == "__main__":
    main()
