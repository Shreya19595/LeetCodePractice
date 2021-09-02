#!/usr/bin/python

'''
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
'''

import string

def main():
    sentence = input("Enter the sentence: ")
    if sentence.islower() == False:
        print("False")
    elif 1 <= len(sentence) <= 1000:
        print(set(string.ascii_lowercase).issubset(set(sentence)))
    else:
        print("False")

if __name__ == "__main__":
    main()
