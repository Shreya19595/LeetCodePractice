#!/usr/bin/python

'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
'''
def main():
    n = int(input("Enter number of steps : "))
    
    steps = [1] * (n+1)
    steps[1] = 1
    
    for i in range(2,n+1):
        steps[i] = steps[i-1] + steps[i-2]

    print(steps[n])

if __name__ == "__main__":
    main()
