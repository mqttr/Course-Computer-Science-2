from math import prod
import sys

def add(values: list) -> float:
    sum = 0
    for val in values:
        sum += float(val)
    return sum

def subtract(values: list):
    total = values[0]
    for val in values[1:-1]:
        total = total - val
    return total

def multiply(values: list):
    product = 1
    for val in values:
        product = float(val) * product
    return product

def modulo(values: list):
    return values[0] % values[1]

def divide(values: list):
    return values[0] / values[1]

def root(values):
    return float(values[0])**( float(values[1]) )

if __name__ == "__main__":
    exit()