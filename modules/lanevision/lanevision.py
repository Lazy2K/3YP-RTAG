"""
Lane detection module.
"""
import numpy as np
import cv2 as cv
from cv2.typing import MatLike

# Import config here


# You should apply config settings here instead of hard coded numbers
def gray_scale(frame: MatLike) -> MatLike:
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


def gausian_blur(frame: MatLike) -> MatLike:
    return cv.GaussianBlur(frame, (5, 5), 0)


def edge_detect(frame: MatLike) -> MatLike:
    return (cv.Canny(frame, 100, 200))


def white_mask(frame: MatLike) -> MatLike:
    return cv.inRange(frame, 100, 200)
