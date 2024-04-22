import cv2

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('t'):
        ENABLED = not ENABLED


def image_text(picture, text):
    return cv2.putText(picture, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (20, 205, 215), 10)




