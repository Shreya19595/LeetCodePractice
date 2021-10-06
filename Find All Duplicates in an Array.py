#!/usr/bin/python

'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.
'''

def main():

    nums = list(map(int, input("Enter nums: ").strip().split()))
    a = []
    for num in nums:
        num = abs(num)
        if(nums[num - 1] > 0):
            nums[num - 1] *= -1
    
        else:
            a.append(num)
    
    print(a)

if __name__ == "__main__":
    main()
