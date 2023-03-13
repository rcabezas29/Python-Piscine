import sys

if __name__ == '__main__':
    s = ""
    for arg in sys.argv[1:]:
        word = ""
        for c in arg:
            if c.islower():
                word += c.capitalize()
            elif c.isupper:
                word += c.lower()
        s += word + " "
    print(s[::-1])