#!/usr/bin/python

def main():
    sentence = input("Enter the Sentence : ")
    k = int(input("Enter number of words to be truncated : ")
    s = sentence.split()
    out = ""

    for i in range(len(s)):
        if (i < k):
            out += s[i] + " "
    print(out[:-1])

if __name__ == "__main__":
    main()
