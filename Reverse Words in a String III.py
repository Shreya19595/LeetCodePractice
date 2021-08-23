#!/usr/bin/python

'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

def main():
    s = input("Enter sentence: ").strip().split()        
    out = []
    for word in s:
        i = 0
        j = (len(word) - 1)
        while (i < j):
            word = list(word)
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        a = (''.join(word))
        out.append(a)
    print(' '.join(out))

    
if __name__ == "__main__":
    main()
