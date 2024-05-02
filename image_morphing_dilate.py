import cv2
import numpy as np

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('D'):
        ENABLED = not ENABLED


def image_morphing_dilate(picture):
    # In cases  like noise removal, erosion is followed by dilation.
    # Because, erosion removes white noises, but it also shrinks our object.
    # So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
    # It is also useful in joining broken parts of an object.
    kernel = np.ones((5, 5), np.uint8)
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    return cv2.dilate(picture, kernel, iterations=1)

