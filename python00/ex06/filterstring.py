from sys import argv
from ft_filter import filter


def is_valid_string(string):
    """Check if string is valid according to exercise rule

    All char must be printable and none punctuation char
    """

    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in string:
        if c in punctuation or c.isprintable() is False:
            return True
    return False


def main():
    """Print a list of words from S that have a length greater than N

    Usage: python filterstring.py <S> <N>
    """

    if len(argv) != 3 or is_valid_string(argv[1]):
        print("AssertionError: the arguments are bad")
    else:
        try:
            N = int(argv[2])
            words = argv[1].split()

            print([e for e in filter(lambda s: len(s) > N, words)])
        except ValueError:
            print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
