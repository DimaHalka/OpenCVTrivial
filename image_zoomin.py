import cv2

ENABLED = False
SHIFT_X = 0
SHIFT_Y = 0

def test_key(key):
    global ENABLED, SHIFT_X, SHIFT_Y
    if key == ord('z'):
        ENABLED = not ENABLED
    if key & 0xFF == 0:  # Up
        SHIFT_Y -= 10
    if key & 0xFF  == 1:  # Down
        SHIFT_Y += 10
    if key & 0xFF == 2:  # Left
        SHIFT_X -= 10
    if key & 0xFF == 3:  # Right
        SHIFT_X += 10

def image_zoomin(picture):
    picture_width, picture_height = picture.shape[1], picture.shape[0]
    center = (picture_width // 2 + SHIFT_X, picture_height // 2 + SHIFT_Y)
    rotation_angle = 0
    scale_factor = 4
    rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, scale_factor)
    return cv2.warpAffine(picture, rotation_matrix, (picture_width, picture_height))

