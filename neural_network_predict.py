from keras.models import load_model
import roi
import cv2
import numpy as np

model = load_model('my_model.h5');


def predict(region):

    # cv2.imshow('ae',region)
    # cv2.waitKey(4000)
    #kernel = np.ones((5, 5), np.uint8)
    #region = cv2.morphologyEx(region, cv2.MORPH_OPEN, kernel)

    a = model.predict_classes(region.reshape(1, 1, 28, 28).astype('float32'))
    # print(a)
    return a
