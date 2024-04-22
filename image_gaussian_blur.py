import cv2

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('g'):
        ENABLED = not ENABLED


def image_gaussian_blur(picture):
    return cv2.GaussianBlur(picture, (9, 9), 0)
