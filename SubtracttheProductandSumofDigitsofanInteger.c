#include <stdio.h>

/*Given an integer number n, return the difference between product of its digits and the sum of its digits.*/

int main()
{
    int n;
    scanf("Enter number: %d\n, n);
    int prod, sum, result;
    sum = 0;
    prod = 1;
    while(n > 0) {
        int a = n % 10;
        sum += a;
        prod *= a;
        n /= 10;
    } 
    result = prod - sum;
    printf("%d\n", result);
    return 0;
}
