import sys

def main():
    if len(sys.argv) <= 1:
        sys.exit('Need to provide operator')
    elif len(sys.argv) <= 3:
        sys.exit('Need to provide at least two values')
    else:
        operator = sys.argv[1]
        values = [float(value) for value in sys.argv[2:]]
        match operator:
            case 'add':
                print(f'Answer = {add(values):.2f}')
            case 'subtract':
                print(f'Answer = {subtract(values):.2f}')
            case 'multiply':
                print(f'Answer = {multiply(values):.2f}')
            case 'divide':
                print(f'Answer = {divide(values):.2f}')
            case _:
                sys.exit('Valid operator names (add, subtract, multiply, divide)')





def add(values):
    lst = [value for value in values if value < 0]
    return sum(lst) if len(lst) != 0 else 0


def subtract(values):
    lst = [value for value in values if value > 0]
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        ans = lst[0]
        for value in lst[1:]:
            ans -= value
        return ans


def multiply(values):
    lst = [value for value in values if value != 0]
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        result = lst[0]
        for value in lst[1:]:
            result *= value
        return result


def divide(values):
    result = values[0]
    for value in values[1:]:
        if value == 0:
            sys.exit('Cannot divide by 0')
        result /= value
    return result


if __name__ == '__main__':
    main()