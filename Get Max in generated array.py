#!/usr/bin/python

'''
You are given an integer n. An array nums of length n + 1 is generated in the following way:
nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.
'''

def main():
    n = int(input("Enter size of array : "))
    nums = [0]*(n+1)
    
    if n == 0:
        return 0
    
    nums = [0] * (n + 1)
    nums[1] = 1
    
    for i in range(2, n + 1):
        
        if (i % 2 == 0):
            nums[i] = nums[(i // 2)]
        else:
            nums[i] = nums[(i // 2)] + nums[(i // 2) + 1]
            
    print(max(nums))

if __name__ == "__main__":
    main()
        
