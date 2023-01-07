import random

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    if not isinstance(text, str):
        print("ERROR")
        exit(1)
    words = text.split(sep)
    match option:
        case "shuffle":
            random.shuffle(words)
        case "unique":
            appear =[]
            for word in words:
                if word in appear:
                    continue
                appear.append(word)
            words = appear
        case "ordered":
            words.sort()
    for word in words:
        yield word
    
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, " ", "shuffle"):
    print(word)