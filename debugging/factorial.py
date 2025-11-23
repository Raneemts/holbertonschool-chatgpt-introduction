#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1        # <-- FIX: decrease n so the loop ends
    return result

f = factorial(int(sys.argv[1]))
print(f)
