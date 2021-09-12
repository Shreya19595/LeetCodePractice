#!/usr/bin/python

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

import string

def main():
    s = input("Enter the String containing brackets: ")
    paradict = {'(' : ')', '[' : ']', '{' : '}'}
        
    a = []
    
    for i in s:
        if i in paradict:
            a.append(paradict[i])
        elif len(a) > 0 and i == a[-1]:
            a.pop()
        else:
            print("False")
    
    if len(a) == 0:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
