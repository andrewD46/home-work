#!/usr/bin/python3.8
# -*- coding: utf-8 -*-


def swap_numbers(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


if __name__ == "__main__":
    first_number = int(input("Enter the number a:"))
    second_number = int(input("Enter the number b:"))
    swap = swap_numbers(first_number, second_number)
    print("a =", swap[0], "\nb =", swap[1])
