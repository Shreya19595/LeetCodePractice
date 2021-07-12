#!/usr/bin/python

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
'''

def main():
    nums = list(map(int,input("Enter the array : ").strip().split()))
    n = len(nums)
    nums.sort()

    if (n == 0):
        return False
    
    for i in nums:
        if (nums.count(i) == 1):
            print(i)

if __name__ == "__main__":
    main()
