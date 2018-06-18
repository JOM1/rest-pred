from flask import Flask, abort, request
from flask_restful import Resource, Api
from boto_client import get_file
from classify_image import run_inference_on_image

app = Flask(__name__)
api = Api(app)



class ImagePred(Resource):
    def get(self, bucket_name, object_name):
        s3_img = get_file(bucket_name, object_name)
        return run_inference_on_image(s3_img.read())

api.add_resource(ImagePred, '/pred/<string:bucket_name>/<string:object_name>')


@app.errorhandler(404)
def not_found(e):
    return '', 404

if __name__ == '__main__':
    app.run(host='127.0.0.1' ,port=5000)
