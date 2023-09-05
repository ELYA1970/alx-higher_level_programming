#!/usr/bin/python3
def print_last_digit(number):
    mod = 10
    o = abs(number) % mod
    print(f"{o}", end='')
    return o
