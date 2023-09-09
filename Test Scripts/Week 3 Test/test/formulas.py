import sys


# formulas for Lab 3 module
def add(values):
    sum = 0
    for val in values:
        if val > 0:
            sum += val
    return sum


def subtract(values):
    difference = 0
    for val in values:
        if val < 0:
            difference += val
    return difference


def multiply(values):
    product = 1
    for val in values:
        if val != 0:
            product *= val
    return product

def divide(values):
    quotient = 0
    if values[0] == 0:
        for i in range(1, len(values)):
            if values[i] == 0:
                sys.exit("Cannot divide by 0")
        return 0
    else:
        quotient = values[0]
    for i in range(1, len(values)):
        if values[i] != 0:
            quotient /= values[i]
        else:
            sys.exit("Cannot divide by 0")
    return quotient