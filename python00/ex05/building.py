from sys import argv, stdin


def sums_of_chars_by_type(text: str) -> str:
    """Calculate the sums of each character grouping by type"""
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punctuation = 0

    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        elif c.isprintable():
            punctuation += 1

    result = f"The text contains {len(text)} characters:\n"
    result += f"{upper} upper letters\n"
    result += f"{lower} lower letters\n"
    result += f"{punctuation} punctuation marks\n"
    result += f"{space} spaces\n"
    result += f"{digit} digits"
    return result


def main():
    """Retrieve the 1st argument and run sums_of_chars_by_type() with it"""
    if (args := len(argv)) > 2:
        print("AssertionError: Usage => python building.py [\"some text\"]")
    elif (args == 2):
        print(sums_of_chars_by_type(argv[1]))
    else:
        s = input("test => ")
        print(s)
        print(len(s))
        print(sums_of_chars_by_type(input("What is the text to count?\n")))


if __name__ == "__main__":
    main()
