import cv2

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('r'):
        ENABLED = not ENABLED


def image_resize(picture):
    return cv2.resize(picture, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_LINEAR)

