#!/usr/bin/bash

import sys

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_factors(n):
    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            return i, n // i

def main():
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <input_file>")
        return

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        n = int(file.readline().strip())

    p, q = find_prime_factors(n)

    print(f"{n}={p}*{q}")

if __name__ == "__main__":
    main()

