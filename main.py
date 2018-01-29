import numpy as np
import cv2
import line_detection as l
import matplotlib.pyplot as plt


cap = cv2.VideoCapture('videos/video-9.avi')

ret, firstFrame = cap.read()

l.get_blue(firstFrame)
l.get_green(firstFrame)
