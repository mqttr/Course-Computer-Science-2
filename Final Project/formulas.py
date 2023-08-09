from math import prod
import sys

def add(values) -> float:
    sum = 0
    for val in values:
        sum += float(val)
    return sum

def subtract(values):
    total = values[0]
    for val in values[1:-1]:
        total = total - val
    return total

def multiply(values):
    product = 1
    for val in values:
        product = float(val) * product
    return product

def modulo(values):
    return values[0] % values[1]

def divide(values):
    return values[0] / values[1]

def root(values):
    return float(values[0])**( float(values[1]) )

if __name__ == "__main__":
    exit()