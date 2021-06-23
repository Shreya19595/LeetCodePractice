#!/usr/bin/python

'''
Given the array candies and the integer extraCandies, where candies[i]
represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among
the kids such that he or she can have the greatest number of candies
among them. Notice that multiple kids can have the greatest number of candies.
'''

def main():
    
    n = int(input("Enter number of kids : "))
    candies = list(map(int,input("Enter the number of candies each kid has : ").strip().split()))[:n]
    extra = int(input("Enter the extra candy count : "))

    for i in range(0, n):
        a = candies[i] + extra
        if (a >= max(candies)):
            print("true")
        else:
            print("false")

if __name__ == "__main__":
    main()
