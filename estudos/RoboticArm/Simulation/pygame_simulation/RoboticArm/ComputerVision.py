import numpy as np
import cv2
from matplotlib import pyplot as plt


def opencv_test(surface_array):
    print(surface_array.shape)
    surface_array = np.transpose(surface_array, axes=[1, 0, 2])
    print(surface_array.shape)
    cv2.imshow('image', surface_array)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # plt.imshow(surface_array)
    # plt.show()


