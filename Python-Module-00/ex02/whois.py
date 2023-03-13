import sys

try:
    assert sys.argv.__len__() == 2, "more than one argument are provided"
    assert sys.argv[1].isnumeric(), "argument is not an integer"
    if int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as msg:
    print(msg)
    exit(1)
