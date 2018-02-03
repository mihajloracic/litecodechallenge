from keras.models import load_model
import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

model = load_model('my_model.h5');


def predict(area):
    return model.predict_classes(area.reshape(1,1,28,28).astype('float32'));
