import cv2
import matplotlib.pyplot as plt

ENABLED = False


def test_key(key):
    global ENABLED
    if key == ord('h'):
        ENABLED = not ENABLED


def image_histogram(picture):
    if len(picture.shape) >= 3:
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
        
    hist = cv2.calcHist([picture], [0], None, [256], [0,256])

    # Plot histogram
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
