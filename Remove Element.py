#!/usr/bin/python

'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

def main():
    nums = list(map(int, input("Enter the array: ").strip().split()))
    val = int(input("Enter number: "))

    l = len(nums)
    i = 0
    j = l - 1
    k = 0
    while(i <= j):
        if nums[i] == val and nums[j] == val:
            k += 1
            j -= 1
        elif nums[i] == val and nums[j] != val:
            k += 1
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
            
    return (l - k)

if __name__ == "__main__":
    main()
