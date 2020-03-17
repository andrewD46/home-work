#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import random

if __name__ == "__main__":
    number = random.randint(0, 100)
    attempt_count = 0
    user_number = 0

    while True:
        attempt_count += 1
        user_number = int(input("Угадайте число: "))

        if user_number > number:
            print("Меньше")
        elif user_number < number:
            print("Больше")

        if user_number == number:
            print("Это загаданное число. \nКоличество попыток:", attempt_count)
            break
