#include <stdio.h>

/*Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.*/

int main()
{ 
    int nums[50];
    for(int i = 0; i < 50; i++)
    {
        scanf("Enter elements of array: %d\n", nums[i]); 
    }
    int min, max;
    min = nums[0];
    max = nums[0];
    for(int i = 0; i < numsSize; i++)
    {
        if(nums[i] > max)
        {
            max = nums[i];
        }
        else if(nums[i] < min)
        {
            min = nums[i];
        }  
        else
        {
            continue;
        }
    }
    int gcd(int a, int b)
    {
        if (a == 0)
           return b;
        if (b == 0)
           return a;
 
        if (a == b)
            return a;
 
        if (a > b)
            return gcd(a-b, b);
        return gcd(a, b-a);
    }
    
    int fin = gcd(max, min);
    printf("%d", fin);
    return 0;
}