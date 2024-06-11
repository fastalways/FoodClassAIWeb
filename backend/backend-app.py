import os
from datetime import datetime
from flask import Flask, flash, redirect, jsonify, request, url_for
from flask_cors import CORS,cross_origin
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2 as cv
import hashlib
import json


directory = os.getcwd()
print(f'Run code at {directory}.\n\n')

class_names_55classes = ['Ba-Mee-Kiao-Ped-Yang', 'Ba-Mee-Krob-Rat-Na', 'Boiled Chicken Rice', 'Bua-Loi', 'Cherri', 'Kaeo-Mangkon', 'Khai-Hong', 'Khanom-Jeen-Kaeng-Khiao-Wan-Kai', 'Khanom-Jeen-Nam-Ngiao', 'Khanom-Khuai', 'Khanom-Phing', 'Khanta-Lup', 'Khao-Phod', 'Khao-Soi-Kai', 'Khao-Soi-Moo', 'Khao-Tom-Mat', 'KhaoKangKareeGai', 'KhaoKhaMoo', 'KhaoKhaiJeow', 'KhaoKlukKapi', 'KhaoKrapaoMooGrob', 'KhaoKungTodKratiem', 'KhaoMooDaeng', 'KhaokapraomoosubKhaiDow', 'Klauy-Khai', 'Kluai-Buat-Chi', 'Kra-Mae', 'Kuai-Chap', 'Kuai-Tiao-Sen-Lek-Tom-Yum-Moo', 'Kuai-Tiao-Sen-Yai-Rat-Na-Kai', 'Kuai-Tiao-Tom-Yum-Kung', 'Kui-Chai-Thot', 'Malako', 'Nam-Aoi-Sai-Kaew', 'Nam-Coke-Sai-Kaew', 'Nam-Krajiab-Sai-Kaew', 'Nam-Lam-Yai-Sai-Kaew', 'Nam-Ma-Khuea-Thet-Sai-Kaew', 'Nam-Ma-Nao-Sai-Kaew', 'Nam-Ma-Tum-Sai-Kaew', 'Nam-Ngon-Sai-Kaew', 'Nam-Sapparot-Sai-Kaew', 'Nam-Som-Khan-Sai-Kaew', 'Ngao', 'Noina', 'Pa-Thong-Ko', 'Rice with Pork Leg Stew', 'Sa-Rim', 'Thurian', 'chompu', 'kaonaped', 'khao kaprao moosub Khai Dow', 'khao mok gai', 'khaomokgai', 'khaomootod']


# -------------- Tensor-flow load model ------------

# 41 Classes Classification Model
model_55classes_path = './model/EfficientNetB4-epoch0800.pb'
model_55classes = tf.keras.models.load_model(model_55classes_path)


# generate different colors for different classes 
COLORS = np.random.uniform(0, 255, size=(len(class_names_55classes), 3))

app = Flask(__name__,static_url_path='/static')
#app.config['SECRET_KEY'] = 'Lady Gaga, Bradley Cooper - Shallow (from A Star Is Born) (Official Music Video)'
#cors = CORS(app, resources={r"/*": {"origins": "https://medwaste-ai.gezdev.com/"}})
#app.config['CORS_ORIGINS'] = ['https://medwaste-ai.gezdev.com']
#app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app)
app.config['JSON_SORT_KEYS'] = False
#CORS(app)

@app.route('/')
#@cross_origin(origin='https://medwaste-ai.gezdev.com',headers=['Content-Type','Authorization'])
#@cross_origin(origin='*')
def show_index():
    str =  """<!DOCTYPE html>
<html>
<head>
<title>Food-Prediction-BACKEND-API</title>
</head>
<body>

<h1>Welcome to Food-Prediction-BACKEND-API</h1>
<p>This is Food-Prediction-BACKEND-API</p>
<p>use POST method to interact with the API</p>
<p>/class55 <- with file that contain picture to classify medical_waste 41 classes </p>
</body>
</html>"""
    return str

ALLOWED_EXTENSIONS = set(['bmp', 'png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.config['im_cache_path'] = './im_cache/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
def hash_str(str):
    return hashlib.sha256(str.encode('utf-8')).hexdigest()


def predictClassify_55classes(im_path):
    img = image.load_img(im_path, target_size=(456, 456)) # B5 -> img_height_width=456
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    prediction = model_55classes.predict(img_preprocessed)
    predict_probs = {class_names_55classes[i]: prediction[0][i]*100.0 for i in range(len(class_names_55classes))}
    sorted_predict_probs = dict(sorted(predict_probs.items(), key=lambda item: item[1], reverse=True))
    #print(sorted_predict_probs)
    return sorted_predict_probs


@app.route('/class55', methods=['POST'])
#@cross_origin(origin='https://medwaste-ai.gezdev.com',headers=['Content-Type','Authorization'])
#@cross_origin(origin='*')
def classify41():
    im_path = ''
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    #str_date = request.form['date']
    success = False
    predict_message = ""
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No selected file'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        im_path = os.path.join(app.config['im_cache_path'], filename)
        file.save(im_path)
        #predict_message = predictClassify_41classes(im_path) # for debug
        try:
            predict_message = predictClassify_55classes(im_path)
            success = True
        except:
            success = False
    else:
        resp = jsonify({'message': im_path + ' -> File type is not allowed'})
        resp.status_code = 400
        return resp
    if success:
        resp = jsonify(predict_message)
        #resp.headers.add("Access-Control-Allow-Origin", "*")
        #resp.headers.add("Access-Control-Allow-Headers", "*")
        #resp.headers.add("Access-Control-Allow-Methods", "*")
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': "Internal AI ERROR"})
        resp.status_code = 500
        return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=False)
