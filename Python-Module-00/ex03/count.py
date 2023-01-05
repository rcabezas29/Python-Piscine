import string

def text_analyzer(text=""):
    """Takes a text and counts the number of lower-case, upper-case, punctuation mark and space characters"""
    if text == "":
        text = input('Input text: ')
    u = 0
    l = 0
    p = 0
    s = 0
    for c in text:
        if c.islower():
            l += 1
        elif c.isupper():
            u += 1
        elif c in string.punctuation:
            p += 1
        elif c.isspace():
            s += 1
    print(f'- {u} upper letter(s)')
    print(f'- {l} lower letter(s)')
    print(f'- {p} punctuation mark(s)')
    print(f'- {s} space(s)')
    
if __name__ == "__main__":
    text_analyzer('Python')
