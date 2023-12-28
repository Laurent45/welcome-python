from sys import argv

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def to_morse(char):
    """
    Convert char to morse code

    This function only support alphanumeric ascii char and space.
    If the char is not support, it raise a ValueError
    """

    if char.isascii() and (char.isalnum() or char == " "):
        return NESTED_MORSE[char.upper()]
    else:
        raise ValueError


def main():
    """Convert and print the string to morse code"""

    if len(argv) != 2:
        print("AssertionError: the arguments are bad")
    else:
        try:
            print(" ".join(to_morse(c) for c in argv[1]))
        except ValueError:
            print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
