#!/usr/bin/python

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def main():
    prices = list(map(int, input("Enter the list: ").strip().split()))

    maxPro = 0
    start = prices[0]
    
    for i in prices:
        if i < start:
            start = i
        elif i > start:
            profit = i - start
            if profit > maxPro:
                maxPro = profit
    print(maxPro)

if __name__ == "__main__":
    main()
