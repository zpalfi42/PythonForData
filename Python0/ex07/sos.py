"""_summary_
"""

import sys

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


def main():
    """_summary_
    """
    try:
        if len(sys.argv) != 2 or sys.argv[1].isalnum() is False:
            raise AssertionError("the argument are bad")
        print(' '.join(NESTED_MORSE[x] for x in sys.argv[1].upper()))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        sys.exit()
