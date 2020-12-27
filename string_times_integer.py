#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program prints the string the number of times specified by the integer

def main():
    # This function prints the string the number of times
    # specified by the integer

    string = input("String: ")
    integer_str = input("Integer: ")
    print("")

    try:
        integer = int(integer_str)
    except Exception:
        print("Invalid Input")
    else:
        if integer > 0:
            while integer > 0:
                print(string, end="")
                integer = integer - 1
        else:
            print("Please enter a positive integer greater than 0")


if __name__ == "__main__":
    main()
