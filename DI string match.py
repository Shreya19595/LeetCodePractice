#!/usr/bin/python

'''
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
'''

def main():
    s = input("Enter the string containing only D and I : ")
    perm = []
    l = len(s)
    x = 0
    for i in range(l):
        if s[i] == "I":
            perm.append(x)
            x += 1
        elif s[i] == "D":
            perm.append(l)
            l -= 1
    perm.append(x)
    print(perm)

if __name__ == "__main__":
    main()
