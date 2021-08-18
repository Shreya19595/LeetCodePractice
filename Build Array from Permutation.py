#!/usr/bin/python

'''
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
'''

def main():
    nums = list(map(int, input("Enter array: ").strip().split()))
    ans = []
    a = 0
    
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    print(ans)

if __name__ == "__main__":
    main()
