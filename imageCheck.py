from flask import Flask, abort, request
from flask_restful import Resource, Api
from boto_client import get_file
from keras.applications.inception_v3 import InceptionV3
from keras.models import load_model
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
import os, sys, io
from PIL import Image


MODEL_NAME='model.h5'
MODEL_PATH='model.h5'
BUCKET_NAME='images'

app = Flask(__name__)
api = Api(app)

if not os.path.exists(MODEL_NAME):
    InceptionV3(include_top=True, weights='imagenet').save(MODEL_PATH)

model = load_model(MODEL_NAME)

# to fix a bug using avital's soulution https://github.com/keras-team/keras/issues/2397
graph = tf.get_default_graph()

def proccess_image(img):

    img = Image.open(io.BytesIO(img.read()))
    img = img.resize((299,299))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # makes values in the range [0, 1]

    return img_tensor

class ImagePred(Resource):
    def get(self, bucket_name, object_name):
        global graph
        with graph.as_default():
            s3_img = get_file(bucket_name, object_name)
            classes = model.predict(proccess_image(s3_img))
            top_pred = decode_predictions(classes)[0][0]
            return '{}, score: {}%'.format(top_pred[1], int(top_pred[2]*100))

api.add_resource(ImagePred, '/pred/<string:bucket_name>/<string:object_name>')


@app.errorhandler(404)
def not_found(e):
    return '', 404

if __name__ == '__main__':
    #MODEL_NAME=sys.argv[1]
    #boto_client.download_file(BUCKET_NAME, MODEL_NAME, MODEL_PATH)
    app.run(host='127.0.0.1' ,port=5000)
