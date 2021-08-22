#!/usr/bin/python

'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

def main():
    nums = list(map(int,input("Enter array: ").strip().split()))
    k = int(input("Enter step: "))
    def twopt(arr, i, j):
        while (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr
    
    if k > len(nums):
        k %= len(nums)
        
    if (k > 0):
        twopt(nums, 0, len(nums) - 1)  # rotate entire array
        twopt(nums, 0, k - 1)          # rotate array upto k elements
        twopt(nums, k, len(nums) - 1)  # rotate array from k to end of array

    print(nums)
    
if __name__ == "__main__":
    main()
