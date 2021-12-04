#!/usr/bin/python

'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

def main():
    strs = list(input("Enter the array: ").strip().split())

    strs.sort()
    
    output = ""
    
    for i in range(len(strs[0])):
        if strs[0][i] == strs[len(strs)-1][i]:
            output += strs[0][i]
        else:
            break
    
    print(output)

if __name__ == "__main__":
    main()
