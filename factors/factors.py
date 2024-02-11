#!/usr/bin/bash

import sys

# Function to factorize a number n into two smaller numbers
def factorize(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

# Function to read numbers from file and factorize them
def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            for factor_pair in factors:
                print(f"{number}={factor_pair[0]}*{factor_pair[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        process_file(file_path)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
    except ValueError:
        print("Invalid input in file.")
        sys.exit(1)
