#!/usr/bin/python

'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return not found.
'''

def main():

    strs = []
    strs = [item for item in input("Enter the words : ").split()]
    def commonword(strs):
        common = []
        for l in strs[0]:
            if all(s.startswith("".join(common)+l) for s in strs): # iterates over every word in srs array and checks if they have common prefix
                common.append(l)
            else:
                break
        return "".join(common)

    prefix = commonword(strs)
    print(prefix)
    
if __name__ == "__main__":
    main()
