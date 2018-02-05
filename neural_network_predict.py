from keras.models import load_model
import roi
import cv2

model = load_model('my_model.h5');


def predict(region):
    gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    scale = roi.scale_to_range(gray)
    resized = roi.resize_region(scale)
    img = cv2.copyMakeBorder(
        resized, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    # cv2.imshow('pred',img)
    # cv2.waitKey(1000000)
    # print(str(model.predict_classes(img.reshape(1,1,28,28).astype('float32'))))

    return model.predict_classes(img.reshape(1,1,28,28).astype('float32'))
