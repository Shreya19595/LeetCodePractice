#!/usr/bin/python

'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums. 
'''

def main():
    nums = list(map(int, input("Enter array: ").strip().split()))
    new = []

    for i in range(len(nums)):
        sums += nums[i]
        new.append(sums)
    print(new)

if __name__ == "__main__":
    main()
        

    
