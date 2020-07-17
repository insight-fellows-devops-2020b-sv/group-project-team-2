


from flask import Flask,  request
import os
import base64
import json
from io import BytesIO

import numpy as np
import requests
from flask import jsonify
from keras.applications import inception_v3
from keras.preprocessing import image

model = None
app = Flask(__name__)
UPLOAD_FOLDER = './upload' #we can change this to s3 address and make changes in some functions

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def ensure_dir(file_path, is_file=False):
    if is_file:
        directory = os.path.dirname(file_path)
    else:
        directory = file_path
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


# def load_model():
#     global model

#     with open('iris_trained_model.pkl', 'rb') as f:
#         model = pickle.load(f)






# @app.route('/model_upload', methods=['GET', 'POST'])
# def upload_model():
#     if request.method == 'POST':
#         if 'file1' not in request.files:
#             return 'there is no file1 in form!'
#         file1 = request.files['file1']
#         data = request.get_json()  # Get data posted as a json
#         data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
#         prediction = model.predict(data)  # runs globally loaded model on the data


#         path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
#         file1.save(path)
#         return path


#         return 'model uploaded'
#     return '''
#     <h1>Upload image for prediction</h1>
#     <form method="post" enctype="multipart/form-data">
#       <input type="file" name="file1">
#       <input type="submit">
#     </form>
#     '''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        img = image.img_to_array(image.load_img(file1, target_size=(224, 224))) / 255.

        # this line is added because of a bug in tf_serving(1.10.0-dev)
        img = img.astype('float16')

        # Creating payload for TensorFlow serving request
        payload = {
            "instances": [{'input_image': img.tolist()}]
        }

        r = requests.post('http://localhost:8501/v1/models/cat_dog:predict', json=payload)

        pred = json.loads(r.content.decode('utf-8'))

        return jsonify(inception_v3.decode_predictions(np.array(pred['predictions']))[0])

        return 'The prediction is:\n'
    return '''
    <h1>Upload image for prediction</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''

# @app.route('/cator____dog/', methods=['POST'])
# def image_classifier():
#     # Decoding and pre-processing base64 image
#     img = image.img_to_array(image.load_img(BytesIO(base64.b64decode(request.form['b64'])),
#                                             target_size=(224, 224))) / 255.

#     # this line is added because of a bug in tf_serving(1.10.0-dev)
#     img = img.astype('float16')

#     # Creating payload for TensorFlow serving request
#     payload = {
#         "instances": [{'input_image': img.tolist()}]
#     }


#     r = requests.post('http://localhost:8501/v1/models/cat_dog:predict', json=payload)


#     pred = json.loads(r.content.decode('utf-8'))


#     return jsonify(inception_v3.decode_predictions(np.array(pred['predictions']))[0])

if __name__ == '__main__':

    # ensure_dir(UPLOAD_FOLDER)
    # load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
