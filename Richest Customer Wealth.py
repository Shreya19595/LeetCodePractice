#!/usr/bin/python

'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
'''

def main():
    i = int(input("Enter number of customers: "))
    j = int(input("Enter number of banks: "))

    acc = [] * i * j
    sums = 0
    new = []

    for k in range(i):
        a = []
        for l in range(j):
            a.append(int(input("Enter wealth: ")))
        acc.append(a)

    for m in acc:
        sums = sum(m)
        new.append(sums)

    new.sort()
    
    print(new[-1])

if __name__ == "__main__":
    main()
        

    
