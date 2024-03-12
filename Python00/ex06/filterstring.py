"""_summary_
"""

import sys

from ft_filter import ft_filter


def main():
    """_summary_
    """
    try:
        if len(sys.argv) != 3 or sys.argv[2].isdigit() is False:
            raise AssertionError("the arguments are bad")
        res = list(ft_filter(lambda x: len(x) > int(sys.argv[2]),
                             (sys.argv[1]).split()))
        print(res)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit()


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        sys.exit()
