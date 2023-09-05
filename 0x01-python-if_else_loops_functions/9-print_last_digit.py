#!/usr/bin/python3
def print_last_digit(number):
    mod = 10
    if number < 0:
        mod *= -1
    o = abs(number) % mod
    return o
