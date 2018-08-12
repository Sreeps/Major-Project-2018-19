import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import png

path = input("Enter the file path ")

image_data = genfromtxt(path, dtype=np.uint8, delimiter=',')
png.from_array(image_data[:, 1:514], 'L').save("output.png")


x = np.uint8(plt.imread('barbara.png')*256)

print(np.array_equal(image_data[:, 1:514], x))


