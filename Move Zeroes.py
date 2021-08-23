#!/usr/bin/python

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''

def main():
    nums = list(map(int,input("Enter array: ").strip().split()))
    j = 0                            #using the two-pointer method
    for i in range(len(nums)):
        if nums[i] != 0 and nums[j] == 0:      #keeping j 1st element fixed until it's non zero
            nums[i], nums[j] = nums[j], nums[i]          
        if nums[j] != 0:
            j += 1
    
if __name__ == "__main__":
    main()
