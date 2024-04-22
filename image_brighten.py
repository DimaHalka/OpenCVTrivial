import cv2
import numpy as np

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('b'):
        ENABLED = not ENABLED


def image_brighten(picture):
    brightness_factor = 1.5
    hsv = cv2.cvtColor(picture, cv2.COLOR_BGR2HSV)
    # hsv[:, :, 2] - This selects the V channel (brightness channel) of the HSV image.
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * brightness_factor, 0, 255)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


def image_auto_brighten(picture):
    target_brightness = 100
    hsv = cv2.cvtColor(picture, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    average_brightness = v.mean()
    scaling_factor = target_brightness / average_brightness
    v_adjusted = cv2.convertScaleAbs(v, alpha=scaling_factor, beta=0)
    hsv_adjusted = cv2.merge([h, s, v_adjusted])
    return cv2.cvtColor(hsv_adjusted, cv2.COLOR_HSV2BGR)

