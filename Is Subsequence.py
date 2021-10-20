#!/usr/bin/python

def main():

    s = input("Enter string s: ")
    t = input("Enter string t: ")

    i = 0
    j = 0
    
    if not s: print("True")
    
    while (i < len(t)):
        if t[i] == s[j]:
            j += 1
            if j == len(s):
                print("True")
        i += 1
    print("False")

if __name__ == "__main__":
    main()
