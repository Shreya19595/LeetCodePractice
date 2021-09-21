#include <stdio.h>

/*Given a binary array nums, return the maximum number of consecutive 1's in the array.*/

int findMaxConsecutiveOnes(int* nums, int numsSize){
    int count = 0;
    int max = 0;
    for(int i = 0; i < numsSize; i++)
    {
        if(nums[i] == 1)
        {
            count++;
            
            if(count > max)
            {
                max = count;
            }
        }
        else
        {
            count = 0;
        }
    }
    return max;
}