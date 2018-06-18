from keras.applications.inception_v3 import InceptionV3
from keras.models import load_model
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
from keras.preprocessing import image
import numpy as np
import os

def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor

if not os.path.exists('model.h5'):
    InceptionV3(include_top=True, weights='imagenet').save('model.h5')

model = load_model('model.h5')

img = load_image('../car.jpg', True)

classes = model.predict(img)

print(decode_predictions(classes))