"""_summary_
"""

import sys
from load_image import ft_load
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def main():
    """_summary_ 
        For showing original image:
            img_show = Image.fromarray(img)
            img_show.show()
        For making it not grayscale (layers=1):
            img2 = img
    """
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)
        img = Image.fromarray(img_array)
        resized = img.crop((300, 200, 700, 600))
        img_grey_array = np.mean(np.array(resized),
                                axis=2, keepdims=True).astype(np.uint8)
        plt.imshow(img_grey_array, cmap='gray', vmin=0, vmax=255)
        print(f"New shape after slicing: {img_grey_array.shape}"
            f" or ({img_grey_array.shape[0]}, {img_grey_array.shape[1]})")
        print(img_grey_array)
        plt.show()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit()


if __name__ == "__main__":
    main()
