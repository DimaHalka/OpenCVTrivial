import cv2

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('o'):
        ENABLED = not ENABLED


def image_rotate(picture):
    picture_width, picture_height = picture.shape[0], picture.shape[1]
    center = (picture_width // 2, picture_height // 2)
    rotation_angle = 60
    scale_factor = 1
    rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, scale_factor)
    return cv2.warpAffine(picture, rotation_matrix, (picture_width, picture_height))


