#!/usr/bin/python

def main():
    n = int(input("Enter number of elements : "))
    nums = list(map(int,input("Enter the numbers : ").strip().split()))[:n]

    num = sorted(nums)
    even = []
    odd = []

    for i in range(n):
        if (num[i] % 2 == 0):
            even.append(num[i])
        else:
            odd.append(num[i])

    num[0::2], num[1::2] = even, odd

    print(num) 

if __name__ == "__main__":
    main()
