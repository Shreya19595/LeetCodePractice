#!/usr/bin/python

'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.
'''

def main():
    n = int(input("Enter size of grid: "))
    grid = []
    nums = []
    for i in range(n):
        nums = list(map(int, input("Enter n numbers for array: ").strip().split()))
        grid.append(nums)

    count0 = 0
    count1 = 0
    final = 0
    mid_sum = 0
    tot_sum = 0
    m = n // 2

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                count1 += 1
            elif grid[i][j] == 0:
                count0 += 1
            if n > 2:
                mid_sum += grid[m][j]
                tot_sum += grid[i][j]
            
    
    if count0 > 0 and mid_sum == 0 and tot_sum != 0:
        final = count1
    elif count0 > 0 and tot_sum == 0 and mid_sum == 0:
        final = count1 + 1
    elif count0 > 0 and tot_sum != 0 and mid_sum != 0:
        final = count1 + 1
    else:
        final = count1
                
    print(final)

if __name__ == "__main__":
    main()
