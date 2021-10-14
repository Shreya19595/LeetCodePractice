#!/usr/bin/python

'''
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
'''

def main():

    nums1 = list(map(int, input("Enter list elements:").strip().split()))
    nums2 = list(map(int, input("Enter list elements:").strip().split()))
    nums3 = list(map(int, input("Enter list elements:").strip().split()))
    
    a = []
    table = defaultdict(int)
    
    # to remove duplicates from each list
    first = list(OrderedDict.fromkeys(nums1)) 
    second = list(OrderedDict.fromkeys(nums2))
    third = list(OrderedDict.fromkeys(nums3))
    
    nums = first + second + third
    
    for i in nums:
        table[i] = table[i] + 1
        if (table[i] >= 2) and (i not in a):
            a.append(i)
    print(a)


if __name__ == "__main__":
    main()
