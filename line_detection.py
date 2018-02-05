import cv2
import numpy as np

n=10000

def get_green(firstFrame1):
    # cv2.imshow('g',firstFrame)
    # cv2.waitKey(n)

    firstFrame = firstFrame1.copy()
    #ignorisanje plave boje
    firstFrame[:, :, 0] = 0

    # cv2.imshow('g',firstFrame)
    # cv2.waitKey(n)

    gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
    ret, t = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    # cv2.imshow('g',gray)
    # cv2.waitKey(n)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(t, 1, np.pi / 180, 100, minLineLength, maxLineGap)

    print('zelene ' + str(len(lines)))

    # for i in range(len(lines)):
    #     for x1, y1, x2, y2 in lines[i]:
    #         cv2.line(firstFrame, (x1, y1), (x2, y2), (255, 255, 0), 2)
    #
    # cv2.imshow('g',firstFrame)
    # cv2.waitKey(n)
    x1 = min(lines[:, 0, 0])
    y1 = max(lines[:, 0, 1])
    x2 = max(lines[:, 0, 2])
    y2 = min(lines[:, 0, 3])
    return [(x1, y1), (x2, y2)]

def get_blue(firstFrame1):
    # cv2.imshow('g',firstFrame)
    # cv2.waitKey(n)
    #ignorisanje zelene boje
    firstFrame = firstFrame1.copy()
    firstFrame[:, :, 1] = 0

    # cv2.imshow('g',firstFrame)
    # cv2.waitKey(n)

    gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
    ret, t = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    # cv2.imshow('g',gray)
    # cv2.waitKey(n)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(t, 1, np.pi / 180, 100, minLineLength, maxLineGap)

    print('plave ' + str(len(lines)))

    x1 = min(lines[:, 0, 0])
    y1 = max(lines[:, 0, 1])
    x2 = max(lines[:, 0, 2])
    y2 = min(lines[:, 0, 3])
    return [(x1, y1), (x2, y2)]
