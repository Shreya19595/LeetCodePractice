include <stdio.h>

/* Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of arr.*/

int main()
{
    int arr, arrSize;
    scanf("Enter size of array:%d\n", arrSize);
    for(int i = 0; i < arrSize; i++)
    {
        scanf("Enter elements:%d\n", arr[i]);
    }

    int answer = 0, n = arrSize;

    for(int i = 0; i < n; i++)
    {
        for(int j = i; j < n; j+=2)
        {
            for(int k = i; k <= j; k++)
                answer += arr[k];
        }
    }
    printf("%d\n", answer);
}