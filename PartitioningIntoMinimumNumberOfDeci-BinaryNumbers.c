#include <stdlib.h>
#include <stdio.h>

/*A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.*/

int minPartitions(char * n){
    int big = 0;
    int size = strlen(n);
    for (int i = 0; i < size; ++i) 
    {
        int num = n[i] - '0';  // removing null character (string end) from the int
        if (num > big) 
        {
            big = num;
        }
    }
    return big;
}