import numpy as np
import cv2
import line_detection as l
import matplotlib.pyplot as plt
import roi
cap = cv2.VideoCapture('videos/video-2.avi')

ret, firstFrame = cap.read()

l.get_blue(firstFrame)
ret, firstFrame = cap.read()
l.get_green(firstFrame)



while cap.isOpened():
    ret, firstFrame = cap.read()

    image_gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
    #img = roi.image_bin(image_gray)
    # img_bin = roi.erode(roi.dilate(img))
    ret,img = cv2.threshold(image_gray, 30, 255, cv2.THRESH_BINARY)

    selected_regions = roi.select_roi(firstFrame.copy())
    #selected_regions = roi.select_roi1(firstFrame.copy(),img)

    #cv2.imshow('g',selected_regions)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()