import cv2

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('E'):
        ENABLED = not ENABLED


def image_histogram_eq(picture):
    if len(picture.shape) >= 3:
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(picture)

