#!/usr/bin/python

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
'''

def main():
    strs = list(input("Enter array: ").strip().split())
    st = {}

    for s in strs:
        sort = ''.join(sorted(s))
        if sort not in st:
            st[sort] = []
        st[sort].append(s)
                
    print(st.values())
                
if __name__ == "__main__":
    main()
