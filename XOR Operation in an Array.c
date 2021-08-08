include <stdio.h>

/* Given an integer n and an integer start.
Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.*/

int main()
{
    int n;
    int start;
    scanf("Enter integer:%d\n, n);
    scanf("Enter start:%d\n, start);

    int xorOperation(int n, int start){
        int num = start;
    
        for (int i = 1; i < n ; i++){
            num ^= (start + 2*i); 
        }
        return num;
    }
    return 0;
}