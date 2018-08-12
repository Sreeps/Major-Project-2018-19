import numpy as np
import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


image_path = input("Enter the image file path ")
x = mpimg.imread(image_path)
x_gray = np.uint8(rgb2gray(x)*256)
(l, w) = x_gray.shape

output_path = input("Enter the output file path ")
with open(output_path, "w") as f:
    for i in range(0, l):
        for j in range(0, w):
            f.write(",")
            f.write(str(x_gray[i][j]))
        f.write("\n")


