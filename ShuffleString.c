#include <stdio.h>
#include <string.h>

/*Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.*/

int main()
{   
    char s;
    int indicesSize = strlen(s);
    int* indices;

    scanf("Enter the string: %s", s);
    
    for(int i = 0; i < len; ++i) 
    {
        scanf("%d", &indices[i]);
    }
  
    char *new = (char*)malloc((indicesSize + 1)*sizeof(char));
    
    for(int i = 0; i < indicesSize; i++)
    {
        new[indices[i]] = s[i];
    }    
    new[indicesSize] = '\0';

    printf("%s", new);
    return 0;
}