#!/usr/bin/python

'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

def main():

    nums = list(map(int, input("Enter nums: ").strip().split()))
    
    n = len(nums)
    if n == 1:
        print(nums[0])
        
    times_table = defaultdict(int)
    
    for i in nums:
        times_table[i] += 1
        if times_table[i] > (n // 2):
            print(i)


if __name__ == "__main__":
    main()
