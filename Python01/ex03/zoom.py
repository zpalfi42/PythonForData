"""_summary_
"""

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
    img = ft_load("animal.jpeg")
    print(img)
    print("AAAAA:")
    img_grey_array = np.mean(img, axis=2, keepdims=True).astype(np.uint8)
    plt.imshow(img_grey_array, cmap='gray', vmin=0, vmax=255)
    plt.show()
    print(img_grey_array)
    # img_show = Image.fromarray(img)
    # # img_show.show()
    # img2 = np.mean(img, axis=2, keepdims=True).astype(np.uint8)
    # # resized = img_show.convert("L")
    # resized = Image.fromarray(img2)  #.crop((0, 0, 400, 400))
    # resized_array = np.array(resized)
    # layers = 1
    # if len(resized_array.shape) > 2:
    #     layers = resized_array.shape[2]
    # print(img)
    # print(f"New shape after slicing: ({resized.size[1]}, {resized.size[0]}, "
    #       f"{layers})")
    # print(resized_array)
    # resized.show()


if __name__ == "__main__":
    main()
