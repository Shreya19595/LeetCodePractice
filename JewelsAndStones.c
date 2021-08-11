#include <stdio.h>
#include <string.h>

/* You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A". */

int main()
{
    char jewels[50];
    char stones[50];
    scanf("Enter Jewels: %s\n", jewels);
    scanf("Enter Stones: %s\n", stones);

    int count = 0;
    for(int i = 0; i < strlen(jewels); i++)
    {
        for(int j = 0; j < strlen(stones); j++)
        {
            if(jewels[i] == stones[j])
            {
                count++;
            }
        }
    }
    printf("%d\n", count);
    return 0;
}