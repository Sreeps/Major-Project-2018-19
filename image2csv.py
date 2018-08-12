import numpy as np
import matplotlib.pyplot as plt

x = np.uint8(plt.imread('barbara.png')*256)
(l, w) = x.shape

with open("output.csv", "w") as f:
    for i in range(0, l):
        for j in range(0, w):
            f.write(",")
            f.write(str(x[i][j]))
        f.write("\n")


