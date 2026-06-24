import numpy as np

from tensorflow.keras.models import load_model

from utils.preprocess import preprocess_image

from utils.labels import CLASS_NAMES

model = load_model("model/image_classifier.h5")


def predict(image_path):

    img = preprocess_image(image_path)

    prediction = model.predict(img)

    index = np.argmax(prediction)

    confidence = float(np.max(prediction))

    label = CLASS_NAMES[index]

    return label, confidence