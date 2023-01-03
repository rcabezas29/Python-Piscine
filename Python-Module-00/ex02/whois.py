import sys

if __name__ == '__main__':
    if sys.argv.__len__() == 1:
        exit(1)
    try:
        assert sys.argv.__len__() == 2, "more than one argument are provided"
        if int(sys.argv[1]) % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    except AssertionError as msg:
        print(msg)
        exit(1)