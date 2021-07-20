#!/usr/bin/python

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

def main():
    word = input("Enter word : ")
    word2 = input("Enter Anagram : ")
    s = list(word2)
    for i in word:
        if i in s:
            s.remove(i)
            continue
        
    if(s == []):
        print("Is Anagram")
    else:
        print("Not Anagram")

if __name__ == "__main__":
    main()
    
