#!/usr/bin/python

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

def main():
    nums1 = list(map(int, input("Enter numbers 1: ").strip().split()))
    nums2 = list(map(int, input("Enter numbers 2: ").strip().split()))
    i , j = 0, 0
    a = []
    
    nums1.sort()
    nums2.sort()
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            a.append(nums1[i])
            i += 1
            j += 1
            
        elif nums1[i] < nums2[j]:
            i += 1
            
        elif nums1[i] > nums2[j]:
            j += 1
            
    print(a)

if __name__ == "__main__":
    main()
