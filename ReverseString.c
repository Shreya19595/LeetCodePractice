#include <stdio.h>
#include <string.h>

/*Write a function that reverses a string. The input string is given as an array of characters s.*/

int main()
{
    char s;
    scanf("Enter a word: %s", s);

    int c;
    for(int i = 0; i < (sSize / 2); i++)
    {
        c = s[i];
        s[i] = s[sSize - 1 - i];
        s[sSize - 1 - i] = c; 
    }
    printf("Reversed String: %s", s);
    return 0;
}