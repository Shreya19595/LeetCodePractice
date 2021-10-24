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
    n = int(input("Enter numbers: "))

    if(n == 0):
            return 0
        elif(n==1 or n == 2):
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        count = 2
        check = 1
        number = 1
        
        while count <= n:
            if(check == 1 and count <= n):
                dp[(number*2)] = dp[number]
                check += 1
                count += 1
            if(check == 2 and count <= n):
                dp[(number*2)+1] = dp[number] + dp[number + 1]
                check = 1
                number += 1
                count += 1
            else:
                count += 1
                
        return max(dp)

if __name__ == "__main__":
    main()
