#include <stdio.h>
#include <math.h>

/*Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.*/

int main()
{
    int recur, n, sum = 0;
    
    scanf("Enter number: %s", n);

    if (n == 1 || n == 7)
    {
        printf("true");
    }    
    else if (n < 10 && n != 1)
    {
        printf("false");
    }

    while(n > 0)
    {
        sum += pow((n % 10), 2);
        n = n / 10;
    }
    
    recur = isHappy(sum);
    
    if (recur == 1 || recur == 7)
    {
        printf("true");
    }
    
    return 0;
}