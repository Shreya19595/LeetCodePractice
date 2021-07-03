#!/usr/bin/python

def main():
    ransom = input("Enter Ransom Note : ")
    mag = input("Enter Magazine contents : ")

    for i in ransom:
        if i in mag:
            ransom = ransom.replace(i,'',1)
        else:
            return False

    if (ransom == ""):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
