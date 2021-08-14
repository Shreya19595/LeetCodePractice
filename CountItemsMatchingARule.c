#include <stdio.h>
#include <string.h>

/*You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
The ith item is said to match the rule if one of the following is true:
ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule. */

int main()
{
    int itemsSize;
    char items[10][3];

    scanf("Enter the number of items: %d", itemsSize);
    
    for(int i = 0; i < itemsSize; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            scanf("%s", items[i][j]);
        }
    }
    
    int count = 0;
    int key = 0;
    if (strcmp(ruleKey, "type") == 0)
    {
        key = 0;
    }
    else if (strcmp(ruleKey, "color") == 0)
    {
        key = 1;
    }
    else if (strcmp(ruleKey, "name") == 0)
    {
        key = 2;
    }

    
    for(int i = 0; i < itemsSize; ++i)
    {
        if (strcmp(items[i][key], ruleValue) == 0)
        {
            count++;
        }   
    }
    printf("%d", count); 
}