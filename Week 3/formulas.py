from math import prod
import sys

def add(values):
    return sum(values)

def subtract(values):
    output = values[0]
    for val in values[1:]:
        output = output - val
    return output

def multiply(values):
    return prod(values)

def divide(values):
    output = values[0]
    if 0 in values[1:]:
        sys.exit("Cannot Divide by 0")
    for val in values[1:]:
        output /= val
    return output

if __name__ == "__main__":
    exit()