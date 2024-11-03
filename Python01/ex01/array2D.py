"""_summary_
"""

import sys
import numpy as np


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
            raise AssertionError("Not correct parameters")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Not correct parameters")
        array = np.array(family)
        print(f"My shape is : {array.shape}")
        newArray = array[start:end]
        print(f"My new shape is : {newArray.shape}")
        return newArray.tolist()
    except AssertionError as e:
        print(f"Error: {e}")
        sys.exit()
