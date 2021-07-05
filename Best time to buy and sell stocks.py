#!/usr/bin/python

def main():
    price = input("Enter Prices : ")
    p = list(map(int, (price.split(" "))))

    minval = p[0]
    maxprofit = 0

    for i in range(1, len(p)):
        if (p[i] < minval):
            minval = p[i]
        elif (p[i] > minval):
            maxprofit += p[i] - minval
            minval = p[i]
    print(maxprofit)
        

if __name__ == "__main__":
    main()
