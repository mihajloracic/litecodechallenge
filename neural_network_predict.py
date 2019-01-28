from keras.models import load_model

model = load_model('my_model.h5');


def predict(region):


    prediction = model.predict_classes(region.reshape(1, 1, 28, 28).astype('float32'))
    return prediction
