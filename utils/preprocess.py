import numpy as np
from tensorflow.keras.preprocessing import image


def preprocess_image(image_path):

    img = image.load_img(image_path, target_size=(32,32))

    img = image.img_to_array(img)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    return img