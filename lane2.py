import numpy as np
import cv2 as cv
from cv2.typing import MatLike


INPUT_CAMERA = cv.VideoCapture(0)
while INPUT_CAMERA.isOpened():
    ret, frame = INPUT_CAMERA.read()

    if not ret:
        print("Error loading frame")
        break

    cv.imshow('frame', frame)
    if (cv.waitKey(1) == ord('q')):
        break

INPUT_CAMERA.release()
cv.destroyAllWindows()
