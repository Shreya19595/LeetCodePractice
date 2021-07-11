#!/usr/bin/python

'''
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
'''

def main():
    ransom = input("Enter Ransom Note : ")
    mag = input("Enter Magazine contents : ")

    for i in ransom:
        if i in mag:
            ransom = ransom.replace(i,'', 1)
            mag = mag.replace(i,'', 1)
        else:
            mag = mag.replace(i,'', 1)

    if (ransom == ""):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
