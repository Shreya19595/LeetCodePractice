#!/usr/bin/python

'''
Given an array of unique integers salary where salary[i] is the salary of the employee i.
Return the average salary of employees excluding the minimum and maximum salary.
'''

def main():

    salary = list(map(int,input("Enter the salary : ").strip().split()))
    n = len(salary)
    total = 0

    for i in range(n):
        for j in range(i+1, n):
            if (salary[i] < salary[j]):
                salary[i], salary[j] = salary[j], salary[i]

    for i in range(1, n-1):
        total +=salary[i]

    average = total // (n-2)

    print(average)
        
if __name__ == "__main__":
    main()
