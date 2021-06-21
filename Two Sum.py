#!/usr/bin/python

'''
Problem statement: Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
'''

def main():
    n = int(input("Enter number of elements : "))
    nums = list(map(int,input("Enter the numbers : ").strip().split()))[:n]
    target = int(input("Enter the sum number : "))
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                print([i,j])
                return    

    print("Not found")
    
if __name__ == "__main__":
    main()

