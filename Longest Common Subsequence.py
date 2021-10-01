#!/usr/bin/python

'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''

def main():

    text1 = input("Enter text1:")
    text2 = input("Enter text2:")
    
    m, n = len(text1), len(text2)
		
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
