import numpy as np
import cv2 as cv
from cv2.typing import MatLike

MASK_MIDPOINT = 600
MASK_BASE = 200


def gray_scale(frame: MatLike) -> MatLike:
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


def gausian_blur(frame: MatLike) -> MatLike:
    return cv.GaussianBlur(frame, (5, 5), 0)


def edge_detect(frame: MatLike) -> MatLike:
    return (cv.Canny(frame, 100, 200))


def white_mask(frame: MatLike) -> MatLike:
    return cv.inRange(frame, 100, 200)


def region_mask(frame: MatLike, triangle_height: int, triangle_base: int) -> MatLike:
    # Find frame width and height
    frame_height, frame_width = frame.shape
    # Define the apex of the triangle mask
    triangle_midpoint = (frame_width // 2, triangle_height)
    # Create cutout shape in an array
    triangle_cutout = np.array(
        [[(0, frame_height - triangle_base), triangle_midpoint, (frame_width, frame_height - triangle_base)]])
    # Gives an empty frame the same shape as the input frame
    frame_mask = np.zeros_like(frame)
    # Fills in the triangle with white pixels
    frame_mask = cv.fillPoly(frame_mask, triangle_cutout, 255)
    # Returns a cutout version of the input frame using the triangle mask
    return cv.bitwise_and(frame, frame_mask)


def detect_lines(frame: MatLike) -> MatLike:
    lines = cv.HoughLinesP(frame, 1, np.pi/180, 10,
                           minLineLength=10, maxLineGap=5)
    if type(lines) != None:
        return lines
    return None


def sort_lines(lines: MatLike):
    left_lines = []
    right_lines = []
    if lines is None:
        return None
    for line in lines:
        x1, y1, x2, y2 = line[0]
        line_details = np.polyfit((x1, x2), (y1, y2), 1)
        line_gradient = line_details[0]
        print("Line gradient is: {}".format(line_gradient))
        if line_gradient > -10 and line_gradient < -0.5:
            left_lines.append(line)
        elif line_gradient < 10 and line_gradient > 0.5:
            right_lines.append(line)
    return (left_lines, right_lines)


INPUT_VIDEO = cv.VideoCapture("assets/video/dashcam/dc1.mp4")
while INPUT_VIDEO.isOpened():
    ret, frame = INPUT_VIDEO.read()

    print("Frame")

    if not ret:
        print("Error loading frame")
        break

    # Image processing
    gray = gray_scale(frame)
    gaus = gausian_blur(gray)
    edge = edge_detect(gaus)
    regi = region_mask(edge, MASK_MIDPOINT, MASK_BASE)

    # Line detection
    lines = detect_lines(regi)
    if lines is not None:

        # All lines
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # cv.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)  # Blue

        # Lane lines
        left_lines, right_lines = sort_lines(lines)

        for line in left_lines:
            x1, y1, x2, y2 = line[0]
            cv.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)  # Red

        for line in right_lines:
            x1, y1, x2, y2 = line[0]
            cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)  # Green

    white = white_mask(gaus)
    mask = region_mask(edge, 550, 100)

    cv.imshow('frame', frame)
    if (cv.waitKey(1) == ord('q')):
        break

INPUT_VIDEO.release()
cv.destroyAllWindows()
