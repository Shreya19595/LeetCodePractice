#!/usr/bin/python

'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
'''

def main():
    s = input("Enter a string using only R and L : ")
    counter = 0
    output = 0
    
    for char in s:
        if char == "R":
            counter +=1
            
        if char == "L":
            counter -=1

        if counter == 0:
            output += 1
    print(output)

if __name__ == "__main__":
    main()
        
