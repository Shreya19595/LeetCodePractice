#!/usr/bin/python

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''

def main():
    nums = list(map(int, input("Enter numbers: ").split().strip()))

    result = [1] * len(nums)        
    for i in range(1, len(nums)):
        result[i] = nums[i-1] * result[i-1]
        
    right_prod = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= right_prod
        right_prod *= nums[i]             
    
    print(result)

if __name__ == "__main__":
    main()
