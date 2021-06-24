#!/usr/bin/python

'''
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
'''

def main():
    n = int(input("Enter count of numbers : "))
    nums = list(map(int,input("Enter the numbers : ").strip().split()))[:n]
    a = 0
    for i in range(0,n):
        for j in range(1,n):
            if (nums[i] == nums[j]) and i < j:
                a = a + 1
            else:
                a = a
    print(a)

if __name__ == "__main__":
    main()

        
            
    
