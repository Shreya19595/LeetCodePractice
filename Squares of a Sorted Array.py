#!/usr/bin/python

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

def main():
    nums = list(map(int,input("Enter array: ").strip().split()))
    output = 0
    def twopointers(arr, n):
        i = 0
        j = n - 1
        while (i <= j):
            if (i < j):
                arr[i] = arr[i] ** 2
                arr[j] = arr[j] ** 2
                i += 1
                j -= 1
            else:                       # for i = j when size of array is odd.
                arr[i] = arr[i] ** 2
                break          
        arr.sort()
        return arr
    
    output = twopointers(nums, len(nums))
    
    print(output)
