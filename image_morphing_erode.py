import cv2
import numpy as np

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('E'):
        ENABLED = not ENABLED


def image_morphing_erode(picture):
    # Erosion: It is useful for removing small white noises.
    # Used to detach two connected objects etc.
    kernel = np.ones((5, 5), np.uint8)
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    return cv2.erode(picture, kernel, iterations=1)

