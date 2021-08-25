#!/usr/bin/python

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

def main():
    nums = list(map(int,input("Enter array: ").strip().split()))
    i = 0
    n = len(nums)
    j = n - 1
        
    new = [0] * n
    k = n - 1
        
    while i <= j:
        if abs(nums[i]) < abs(nums[j]):
            new[k] = nums[j] ** 2
            j -= 1
                
        else:
            new[k] = nums[i] ** 2
            i += 1
        k -= 1
            
    print(new)
    
if __name__ == "__main__":
    main()
