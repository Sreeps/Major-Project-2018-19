import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import png

csv_path = input("Enter the file path ")
image_path = input("Enter the path for the image ")

image_data = genfromtxt(csv_path, dtype=np.uint8, delimiter=',')
png.from_array(image_data[:, 1:514], 'L').save(image_path)


x = np.uint8(plt.imread('barbara.png')*256)

print(np.array_equal(image_data[:, 1:514], x))


