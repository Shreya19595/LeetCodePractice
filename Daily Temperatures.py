#!/usr/bin/python

'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

def main():
    temperature = list(map(int, input("Enter numbers: ").split().strip()))
    stack = []
    n = len(temperature)
    res = [0] * n
    
    for i in range(n):
        t = temperature[i]
        while stack != [] and temperature[stack[-1]] < t:
            less = stack.pop()
            res[less] = i - less
        stack.append(i)
    print(res)

if __name__ == "__main__":
    main()
