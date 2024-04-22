import cv2

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('G'):
        ENABLED = not ENABLED


def image_grayscale(picture):
    return cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
