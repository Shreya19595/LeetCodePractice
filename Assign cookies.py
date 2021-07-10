#!/usr/bin/python

def main():

    g = list(map(int,input("Enter the greed factor : ").strip().split()))
    s = list(map(int,input("Enter the size of cookie : ").strip().split()))
    count = 0
    g.sort()
    s.sort()

    while s and g:
        if g[-1] <= s[-1]:       #starting with last element
            s.pop()
            g.pop()
            count += 1
        else:
            g.pop()
              
    print(count)

if __name__ == "__main__":
    main()
