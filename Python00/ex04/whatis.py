"""_summary_

Raises:
    AssertionError: "more than one argument is provided"
    AssertionError: "argument is not an integer"
"""
import sys

def main():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(sys.argv) < 2:
        sys.exit()
    try:
        x = int(sys.argv[1])
        if x % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as ae:    
        print(f"AssertionError: {ae}")
        sys.exit()
