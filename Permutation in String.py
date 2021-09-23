#!/usr/bin/python

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
'''

import string

def main():
    s1 = input("Enter the first sentence: ")
    s2 = input("Enter the second sentence: ")

    window = len(s1)
    s1_c = Counter(s1)
    
    for i in range(len(s2)-window+1):
        s2_c = Counter(s2[i:i+window])
        if s2_c == s1_c:
            print("True")
        
    print("False")

if __name__ == "__main__":
    main()
