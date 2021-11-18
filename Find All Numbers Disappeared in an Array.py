#!/usr/bin/python

'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''

def main():
    nums = list(map(int, input("Enter numbers: ").strip().split()))
    
    total_set = set(range(1, len(nums)+1))
    nums_set = set(nums)
    
    print(total_set - nums_set)

if __name__ == "__main__":
    main()
