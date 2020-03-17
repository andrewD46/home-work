#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    ball_count = int(input("Enter the number of balls: "))

    if ball_count == 0 or ball_count == 1 or ball_count == 2 or ball_count == 4 or ball_count == 7:
        print("NO")
    else:
        print("YES")
