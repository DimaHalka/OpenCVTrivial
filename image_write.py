import cv2

picture = cv2.imread("IMG_3005.JPG")
picture = cv2.resize(picture,
                     (0, 0),
                     fx=0.2, fy=0.2,
                     interpolation=cv2.INTER_LINEAR)
cv2.imwrite("IMG_3005.Modified.JPG", picture)
