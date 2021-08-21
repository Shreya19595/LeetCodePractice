#!/usr/bin/python

'''
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.
'''

def main():

    nums = list(map(int, input("Enter array: ").strip().split()))
    target = int(input("Enter target number: "))
    result = 0
        
    def binary_search(arr, low, high, x):

        if high >= low:

            mid = (high + low) // 2

            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)

            else:
                return binary_search(arr, mid + 1, high, x)

        else:
            return -1
    
    result = binary_search(nums, 0, len(nums)-1, target)
    print(result)
    
if __name__ == "__main__":
    main()
