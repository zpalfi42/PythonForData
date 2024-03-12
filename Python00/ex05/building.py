"""_summary_
"""

import sys


def count(text: str):
    """Iterates the given str and prints the nmber of characters inside it.
    """
    count_dict = {"total": 0, "upper": 0, "lower": 0, "punct": 0,
                  "spaces": 0, "digits": 0}
    count_dict["total"] += len(text)
    for i in text:
        if i.isupper():
            count_dict["upper"] += 1
        elif i.islower():
            count_dict["lower"] += 1
        elif i.isalnum():
            count_dict["digits"] += 1
        elif i.isspace():
            count_dict["spaces"] += 1
        else:
            count_dict["punct"] += 1
    print(f"The text contains {count_dict['total']} characters:\n"
          f"{count_dict['upper']} upper letters\n"
          f"{count_dict['lower']} lower letters\n"
          f"{count_dict['punct']} punctuation marks\n"
          f"{count_dict['spaces']} spaces\n"
          f"{count_dict['digits']} digits")


def main():
    """Main function where we avoid errors and ask for input.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 2:
            count(sys.argv[1])
        else:
            try:
                text = input()
                count(text)
            except EOFError:
                print()
                sys.exit()
            except KeyboardInterrupt:
                print()
                sys.exit()
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        sys.exit()
