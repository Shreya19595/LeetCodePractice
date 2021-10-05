#!/usr/bin/python

'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.
'''

def main():

    nums = list(map(int, input("Enter nums: ").strip().split()))
    index = list(map(int, input("Enter index: ").strip().split()))

    if len(nums) == 1:
        print(nums[0])

    a = []
    
    for i in range(len(nums)):
        a.insert(index[i], nums[i])
    print(a)


if __name__ == "__main__":
    main()
