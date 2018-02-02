import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

plt.ion()

def resize_region(region):
    '''Transformisati selektovani region na sliku dimenzija 28x28'''
    return cv2.resize(region,(20,20), interpolation = cv2.INTER_NEAREST)


def select_roi(image):
    gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    img, contours, hierarchy = cv2.findContours(
        thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

        (x, y), radius = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        x=int(x)
        y=int(y)
        radius = int(radius)
        if radius < 20 and radius>7:
                #cv2.circle(image, center, radius, (0, 255, 0), 2)
                cv2.rectangle(image, (x - radius, y - radius), (x + radius, y + radius), (0, 255, 0), 2)
                print(radius);
                cv2.circle(image,(x - radius, y - radius),1,(0, 0, 255), 2)
                crop_img = image[y-radius-1:y + radius+1, x-radius-1:x + radius+1]

    return image

def scale_to_range(image): # skalira elemente slike na opseg od 0 do 1
    ''' Elementi matrice image su vrednosti 0 ili 255.
        Potrebno je skalirati sve elemente matrica na opseg od 0 do 1
    '''
    return image/255


def image_bin(image_gs):
    height, width = image_gs.shape[0:2]
    image_binary = np.ndarray((height, width), dtype=np.uint8)
    ret,image_bin = cv2.threshold(image_binary, 127, 255, cv2.THRESH_BINARY)
    return image_bin


def invert(image):
    return 255-image


def dilate(image):
    kernel = np.ones((3,3)) # strukturni element 3x3 blok
    return cv2.dilate(image, kernel, iterations=1)


def erode(image):
    kernel = np.ones((3,3)) # strukturni element 3x3 blok
    return cv2.erode(image, kernel, iterations=1)

def display_image(image, color= False):
    if color:
        plt.imshow(image)
    else:
        plt.imshow(image, 'gray')