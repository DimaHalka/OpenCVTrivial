import cv2
import numpy as np

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('k'):
        ENABLED = not ENABLED


def image_sharpen_kernel(picture):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(picture, -1, kernel)
