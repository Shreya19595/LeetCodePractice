#!/usr/bin/python

'''
Given an n x n matrix where each of the rows and columns are sorted in
ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth
distinct element.
'''

def main():
    n = int(input("Enter the size of matrix : "))
    matrix = []
    a = []
    count = 0

    if n == 0:
        return False

    for i in range(n):                       #inputting in 1-D array because it's quicker to sort
        for j in range(n):
            a.append(int(input()))
    a.sort()

    matrix = [a[r * n:(r +1)*n] for r in range(0, n)]    #converting to n-D array

    k = int(input("Enter element number : "))

    for i in range(n):
        for j in range(n):
            count += 1
            if count == k:
                print(matrix[i][j])
                exit

if __name__ == "__main__":
    main()



    
