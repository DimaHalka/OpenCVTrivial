import cv2

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('m'):
        ENABLED = not ENABLED


def image_median_blur(picture):
    return cv2.medianBlur(picture, 7)

