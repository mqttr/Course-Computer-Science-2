import math

def clean_input(x):
    result = []
    for arg in x:
        value = float( str(arg).strip() )

        if value <= 0:
            raise TypeError

        result.append(value)
    return result

def circle(*args):
    if not len(args) == 1:
        raise ValueError

    values = clean_input( args )
    return math.pi * ( values[0]**2 )

def rectangle(*args):
    if not len(args) == 2:
        raise ValueError

    values = clean_input( args )
    return values[0]*values[1]

def square(*args):
    if not len(args) == 1:
        raise ValueError
    values = clean_input(args)
    return values[0]**2

def triangle(*args):
    if not len(args) == 2:
        raise ValueError

    values = clean_input( args )
    return 1/2 * values[0] * values[1]

if __name__ == "__main__":
    pass