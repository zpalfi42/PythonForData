"""_summary_
"""

from matplotlib import pyplot as plt
import numpy as np


def ft_invert(array: list) -> list:
    """Inverts the color of the images received

    Args:
        list (_type_): _description_

    Returns:
        list: _description_
    """
    result = 255 - array
    plt.imshow(result, vmin=0, vmax=255)
    plt.show()


def ft_red(array: list) -> list:
    """Turns the image to only Red colors

    Args:
        list (_type_): _description_

    Returns:
        list: _description_
    """
    result = np.zeros_like(array)
    result[:, :, 0] = array[:, :, 0]
    plt.imshow(result, vmin=0, vmax=255)
    plt.show()


def ft_green(array: list) -> list:
    """Turns the image to only Green colors

    Args:
        list (_type_): _description_

    Returns:
        list: _description_
    """
    result = np.zeros_like(array)
    result[:, :, 1] = array[:, :, 1]
    plt.imshow(result, vmin=0, vmax=255)
    plt.show()


def ft_blue(array: list) -> list:
    """Turns the image to only Blue colors

    Args:
        list (_type_): _description_

    Returns:
        list: _description_
    """
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    plt.imshow(result, vmin=0, vmax=255)
    plt.show()


def ft_grey(array: list) -> list:
    """Turns the image to only Grey colors

    Args:
        list (_type_): _description_

    Returns:
        list: _description_
    """
    result = np.mean(np.array(array), axis=2, keepdims=True).astype(np.uint8)
    plt.imshow(result, cmap='gray', vmin=0, vmax=255)
    plt.show()
