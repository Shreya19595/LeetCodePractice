#!/usr/bin/python

'''
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
'''

def main():
    n = int(input("Enter number: "))

    output = 0
    m = 0
    if n // 7:
        output = 28
        m = 1
        while(m != n // 7):
            output += 28 + (7 * m)
            m += 1
            
    for i in range(m + 1, n % 7 + m + 1):
        output += i
    
    return output

if __name__ == "__main__":
    main()
