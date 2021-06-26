#!/usr/bin/python

'''
You are given an integer array nums and you have to return a new counts
array. The counts array has the property where counts[i] is the number of
smaller elements to the right of nums[i].
'''

def main():
    
    n = int(input("Enter number of elements : "))
    num = list(map(int,input("Enter the numbers : ").strip().split()))[:n]
    output = []
    
    for i in range(n):
        a = 0
        for j in range(i+1, n):
            if (num[i] > num[j]):
                a = a + 1
            else:
                a = a + 0               
        output.append(a)        #output = output.append(a) throws an error
    print(output)

if __name__ == "__main__":
    main()
            
