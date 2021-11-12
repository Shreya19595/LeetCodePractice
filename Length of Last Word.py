#!/usr/bin/python

'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
'''

def main():

    s = input("Enter the sentence: ")
    a = s.split()
    if(len(a) <= 0):
        print("0")
    else:
        print(len(a[-1]))

if __name__ == "__main__":
    main()
