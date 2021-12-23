import keyword

keys = ["for", "while", "tanisha", "break", "sky",
        "elif", "assert", "pulkit", "lambda", "else", "sakshar"]


def contains_keyword(*arguments):
    for i in range(len(arguments)):
        # checking which are keywords
        if keyword.iskeyword(arguments[i]):
            print(arguments[i] + " True")
        else:
            print(arguments[i] + " False")


print(contains_keyword("Hello", "goodbye"))
