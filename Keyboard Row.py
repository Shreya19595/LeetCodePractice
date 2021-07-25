#!/usr/bin/python

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
