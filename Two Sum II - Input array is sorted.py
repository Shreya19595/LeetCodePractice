#!/usr/bin/python

'''
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''

def main():
    numbers = list(map(int,input("Enter array: ").strip().split()))
    i = 0
    j = len(numbers) - 1
    # using two pointers
    while (i < j):
        if numbers[i] + numbers[j] == target:                
            break
        elif numbers[i] + numbers[j] < target:  #this comparison since the array is in ascending order
            i += 1
        else:
            j -= 1
    ans = [i + 1, j + 1]
    ans.sort()
    return ans
    
if __name__ == "__main__":
    main()
