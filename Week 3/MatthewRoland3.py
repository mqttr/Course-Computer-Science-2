import formulas as f
import sys

def main():
    systemArguments = sys.argv
    if len(systemArguments) <= 1:
        sys.exit("Need to provide the operator name.")
    elif len(systemArguments) == 2:
        sys.exit("Need to provide at least two values.")
    elif len(systemArguments) == 3:
        sys.exit("Need at least 2 values.")
    else:

        floatValueList = [ float(ele) for ele in systemArguments[2:] ]
        if systemArguments[1].lower() == "divide":
            print( format(f.divide(floatValueList), "0.2f"))
        elif systemArguments[1].lower() == "multiply":
            print( format(f.multiply(floatValueList), "0.2f") )
        elif systemArguments[1].lower() == "subtract":
            print( format(f.subtract(floatValueList), "0.2f") )
        elif systemArguments[1].lower() == "add":
            print( format(f.add(floatValueList), "0.2f" ))
        else:
            print("Valid operator names (add, subtract, multiply, divide)")
        


if __name__ == "__main__":
    main()