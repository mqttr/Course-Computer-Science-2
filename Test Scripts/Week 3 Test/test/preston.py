import sys

import formulas


def main():
    arguments = sys.argv
    calculatedValueFromArguments = calculate(arguments)
    print(f"Answer = {calculatedValueFromArguments:.2f}")

def calculate(args):
    if check_args_length(args):
        argumentsFloatList = [float(x) for x in args[2:len(args)]]
        match args[1]:
            case "add":
                return formulas.add(argumentsFloatList)
            case "subtract":
                return formulas.subtract(argumentsFloatList)
            case "multiply":
                return formulas.multiply(argumentsFloatList)
            case "divide":
                return formulas.divide(argumentsFloatList)
            case _:
                sys.exit("Valid operator names (add, subtract, multiply, divide)")



def check_args_length(args):
    if len(args) <= 1:
        sys.exit("Need to provide operator.")
    elif len(args) <= 3:
        sys.exit("Need to provide at least two values.")
    elif len(args) > 3:
        return True


if __name__ == '__main__':
    main()