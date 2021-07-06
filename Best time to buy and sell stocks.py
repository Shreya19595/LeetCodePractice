#!/usr/bin/python

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

def main():
    price = input("Enter Prices : ")
    p = list(map(int, (price.split(" "))))

    minval = p[0]
    maxprofit = 0

    for i in range(1, len(p)):
        if (p[i] < minval):
            minval = p[i]
        elif (p[i] > minval):
            maxprofit += p[i] - minval
            minval = p[i]
    print(maxprofit)
        

if __name__ == "__main__":
    main()
