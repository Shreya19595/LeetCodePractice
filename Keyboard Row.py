#!/usr/bin/python
'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
'''

def main():
    words = list(input("Enter words : ").strip().split())
    row1 = set('qwertyuiopQWERTYUIOP')
    row2 = set('asdfghjklASDFGHJKL')
    row3 = set('zxcvbnmZXCVBNM')
    new = []

    for word in words: 
        w = set(list(word))
        if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
            new.append(word)
    print(new)
    
if __name__ == "__main__":
    main()
