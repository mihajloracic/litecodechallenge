import cv2
import numpy as np

def get_green(firstFrame):
    #ignorisanje plave boje
    firstFrame[:, :, 0] = 0

    gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
    ret, t = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(t, 1, np.pi / 180, 100, minLineLength, maxLineGap)

    print('zelene ' + len(lines).__str__())

    for i in range(len(lines)):
        for x1, y1, x2, y2 in lines[i]:
            cv2.line(firstFrame, (x1, y1), (x2, y2), (255, 255, 0), 2)

def get_blue(firstFrame):
    #ignorisanje zelene boje
    firstFrame[:, :, 1] = 0

    gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
    ret, t = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(t, 1, np.pi / 180, 100, minLineLength, maxLineGap)

    print('plave ' + len(lines).__str__())

    for i in range(len(lines)):
        for x1, y1, x2, y2 in lines[i]:
            cv2.line(firstFrame, (x1, y1), (x2, y2), (255, 255, 0), 2)


