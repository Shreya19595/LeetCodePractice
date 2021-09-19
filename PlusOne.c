#include <stdio.h>
#include <stdlib.h>

/*You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    int n = digitsSize;
    for(int i = n - 1; i >= 0; i--)
    {
        if(digits[i] == 9)
        {
            digits[i] = 0;
        }
        else
        {
            digits[i] = digits[i] + 1;
            *returnSize = n;
             return digits;
        }
    }
    
    // calloc() allocate the memory and set 0 to all of the integers
    
    int* result = (int*)calloc((n + 1), sizeof(int));  

    *returnSize = n + 1;
    
    result[0] = 1;
    return result;
}