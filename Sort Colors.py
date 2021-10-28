#!/usr/bin/python

'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
'''

def main():

    nums = list(map(int, input("Enter the numbers: ").strip().split()))

    swap = True
        
    while swap:
        swap = False
        
        for i in range(len(nums) - 1):
            if nums[i]> nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True
    print(nums)

if __name__ == "__main__":
    main()
