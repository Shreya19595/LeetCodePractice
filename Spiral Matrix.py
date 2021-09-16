#!/usr/bin/python

'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

def main():
    m = int(input("Enter number of rows:"))
    n = int(input("Enter number of columns:"))
      
    matrix = []
    print("Enter entries rowwise:")
      
    for i in range(m):        
        a = []
        for j in range(n):     
             a.append(int(input()))
        matrix.append(a)
    
    output = []

'''
1 - pop the first row and store it in result
2 - rotate the remaining matrix
3 - jump to 1st step.
'''
        
    while matrix:
        output += matrix.pop(0)
        matrix = (list(zip(*matrix)))[::-1]  #slice notation
    
    print(output)
    
if __name__ == "__main__":
    main()
