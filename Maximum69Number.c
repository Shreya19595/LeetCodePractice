#include <stdio.h>

/*Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).*/


int maximum69Number (int num){
    int a = 0;
    int x = 3;
    for (int i = num; i > 1; i /= 10, x *= 10)
    {
        if(i % 10 == 6)
            a = x;
    }
    return num + a;
}