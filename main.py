import cv2

import image_brighten  # b
import image_histogram  # h
import image_histogram_eq  # e
import image_grayscale  # G
import image_gaussian_blur  # g
import image_median_blur  # m
import image_morphing_erode  # E
import image_morphing_dilate  # D
import image_resize
import image_rotate  # o
import image_sharpen_kernel  # k
import image_text  # t
import image_zoomin  # z 

FILE_NAME = 'video.m4v'

video = cv2.VideoCapture(FILE_NAME)

if video.isOpened():
    frame_cnt = 1
    playing = True
    playing_once = False
    while True:
        if playing or playing_once:
            ok, picture = video.read()
            if not ok:
                break

            if image_sharpen_kernel.ENABLED:
                picture = image_sharpen_kernel.image_sharpen_kernel(picture)
            if image_median_blur.ENABLED:
                picture = image_median_blur.image_median_blur(picture)
            if image_morphing_erode.ENABLED:
                picture = image_morphing_erode.image_morphing_erode(picture)
            if image_morphing_dilate.ENABLED:
                picture = image_morphing_dilate.image_morphing_dilate(picture)
            if image_resize.ENABLED:
                picture = image_resize.image_resize(picture)
            if image_zoomin.ENABLED:
                picture = image_zoomin.image_zoomin(picture)
            if image_gaussian_blur.ENABLED:
                picture = image_gaussian_blur.image_gaussian_blur(picture)
            if image_rotate.ENABLED:
                picture = image_rotate.image_rotate(picture)
            if image_text.ENABLED:
                picture = image_text.image_text(picture, f'{frame_cnt}')
            if image_brighten.ENABLED:
                picture = image_brighten.image_auto_brighten(picture)
            if image_grayscale.ENABLED:
                picture = image_grayscale.image_grayscale(picture)
                image_histogram.ENABLED = False
            if image_histogram_eq.ENABLED:
                picture = image_histogram_eq.image_histogram_eq(picture)
            if image_histogram.ENABLED:
                image_histogram.image_histogram(picture)

            cv2.imshow(FILE_NAME, picture)
            playing_once = False
            frame_cnt += 1

        key = cv2.waitKey(20)
        if frame_cnt == 2:
            playing = False
        if key == ord('q'):
            break
        if key == ord('e'):
            playing_once = True
        if key == ord(' '):
            playing = not playing

        image_brighten.test_key(key)
        image_histogram.test_key(key)
        image_histogram_eq.test_key(key)
        image_grayscale.test_key(key)
        image_resize.test_key(key)
        image_median_blur.test_key(key)
        image_morphing_erode.test_key(key)
        image_morphing_dilate.test_key(key)
        image_sharpen_kernel.test_key(key)
        image_zoomin.test_key(key)
        image_gaussian_blur.test_key(key)
        image_rotate.test_key(key)
        image_text.test_key(key)

    video.release()
    cv2.destroyAllWindows()

