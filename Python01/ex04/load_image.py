"""_summary_
"""

import sys
import os
from PIL import Image
from numpy import asarray


def ft_load(path: str) -> list:
    """_summary_

    Args:
        path (str): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_

    Returns:
        list: _description_
    """
    try:
        if os.path.exists(path) is False:
            raise ValueError("File doesn't exist")
        img = Image.open(path)
        if img.format not in ("JPEG", "JPG"):
            raise ValueError("File is not JPEG or JPG")
        print(f"The shape of the image is: ({img.size[1]}, {img.size[0]}, "
              f"{img.layers})")
        return asarray(img)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit()
