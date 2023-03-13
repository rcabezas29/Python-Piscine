import sys

try:
    if sys.argv.__len__() != 3:
        raise ValueError('Wrong number of arguments')
    print(f'Sum: {int(sys.argv[1]) + int(sys.argv[2])}')
    print(f'Difference: {int(sys.argv[1]) - int(sys.argv[2])}')
    print(f'Product: {int(sys.argv[1]) * int(sys.argv[2])}')
    print(f'Quotient: {int(sys.argv[1]) / int(sys.argv[2])}')
    print(f'Remainder: {int(sys.argv[1]) % int(sys.argv[2])}')
except ZeroDivisionError as e:
    print('ERROR (division by zero)')
    print('ERROR (module by zero)')
except ValueError as e:
    print(e)
    