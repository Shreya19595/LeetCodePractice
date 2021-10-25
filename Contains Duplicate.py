#!/usr/bin/python

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

# Sol 1: Using sets

def main():
    nums = list(map(int, input("Enter numbers: ").split().strip()))

    print(len(set(nums)) != len(nums))

if __name__ == "__main__":
    main()


# Sol 2: Using Dictionary

def main():
    nums = list(map(int, input("Enter numbers: ").split().strip()))

    dic = {}
    for i in nums:
        if i in ref:
            print(True)
        dic[i] = 1
    print(False)

if __name__ == "__main__":
    main()
