#!/usr/bin/python

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''

def main():
    nums = list(map(int, input("Enter numbers: ").split().strip()))

    dp = [0] * len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i] + dp[i - 1]:
            dp[i] = nums[i] + dp[i - 1]
        else:
            dp[i] = nums[i]
    print(max(dp))

if __name__ == "__main__":
    main()
