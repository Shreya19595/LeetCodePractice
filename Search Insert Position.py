#!/usr/bin/python

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
'''

def main():
    nums = list(map(int, input("Enter array: ").strip().split()))
    target = int(input("Enter target number: "))

    result = 0
    final = 0
    def binary(arr, low, high, x):
        
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binary(arr, low, mid - 1, x)
            else:
                return binary(arr, mid + 1, high, x)
        else:
            return -1
        
    result = binary(nums, 0, (len(nums)) - 1, target)
    
    if result != -1:
        print(result)
    
    else:
        nums.append(target)
        nums.sort()
        print(nums)
        final = binary(nums, 0, (len(nums)) - 1, target)
        print(final)
        

if __name__ == "__main__":
    main()
