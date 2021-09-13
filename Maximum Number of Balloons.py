#!/usr/bin/python

'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''

import string

def main():
    text = input("Enter the String: ")
    counta = 0
    countb = 0
    countl = 0
    counto = 0
    countn = 0
    for i in text:
        if i == "b":
            countb += 1
        elif i == "a":
            counta += 1
        elif i == "l":
            countl += 1
        elif i == "o":
            counto += 1
        elif i == "n":
            countn += 1
        else:
            continue
            
    countl = countl // 2;
    counto = counto // 2;
            
    print(min(counta, countb, countl, counto, countn))
        

if __name__ == "__main__":
    main()
