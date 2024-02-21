"""_summary_
"""

import sys
from ft_filter import ft_filter


def main():
    """_summary_
    """
    print("\033[01mFilter tester:")
    cases = [
        ('Hello the World', 4),
        ('Hello thw World', 99),
        ('A n o t h e r', 1),
        ('A n o t h e r', 0),
        ('Lorem ipsum dolor sit amet onsectetur adipiscing elit Nunc dolor '
         'augue pretium vitae euismod a interdum vel leo Pellentesque semper'
         ' convallis odio', 5)
    ]

    for text, n in cases:
        print(f"\033[34mCase ({text}, {n}):")
        res1 = list(ft_filter(lambda x: len(x) > n, text.split()))
        res2 = list(filter(lambda x: len(x) > n, text.split()))
        if res1 == res2:
            print("\033[32mSuccess")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        sys.exit()
