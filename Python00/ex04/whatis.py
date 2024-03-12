"""_summary_

Raises:
    AssertionError: _description_
    AssertionError: _description_
"""
import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) < 2:
            sys.exit()
        if sys.argv[1].isdigit():
            x = int(sys.argv[1])
            if x % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        else:
            raise AssertionError("argument is not an integer")
    except AssertionError as ae:
        print(f"AssertionError: {ae}")
        sys.exit()
