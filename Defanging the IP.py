#!/usr/bin/python

def main():
    IP = input("Enter an IP address : ")
    newIP = ""

    for c in IP:
        if c == ".":
            newIP += "[.]"
        else:
            newIP += c
    print(newIP)

if __name__ == "__main__":
    main()
