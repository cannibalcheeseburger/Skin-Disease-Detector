from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow.keras.models as models

def predict():
    test_image = image.load_img('./temp/temp.jpg', target_size = (256, 256))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    model = models.load_model('best_model.h5')
    result = model.predict(test_image)
    return np.argmax(result)