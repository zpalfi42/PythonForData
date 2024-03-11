"""_summary_
"""

import sys


def slice_me(family: list, start: int, end: int) -> list:
    """_summary_

    Args:
        family (list): _description_
        start (int): _description_
        end (int): _description_

    Returns:
        list: _description_
    """
    try:
        if isinstance(family, list) is False or \
                isinstance(start, int) is False or \
                isinstance(end, int) is False or\
                len(family) < 1:
            raise ValueError("Not correct parameters")
        max_len = 0
        for item in family:
            if max_len != 0 and len(item) != max_len:
                raise ValueError("Lists are not the same size")
            max_len = len(item)
        x = slice(start, end)
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        print(f"My new shape is : ({len(family[x])}, {len(family[0])})")
        return family[x]
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit()
