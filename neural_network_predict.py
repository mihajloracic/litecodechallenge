from keras.models import load_model
import roi
import cv2

model = load_model('my_model.h5');


def predict(region):

    # cv2.imshow('ae',region)
    # cv2.waitKey(4000)

    a = model.predict_classes(region.reshape(1, 1, 28, 28).astype('float32'))
    # print(a)
    return a
