import datetime

import cv2
import numpy as np
from flask import Flask, render_template, request

from flaskr import app
import flaskr.main_test as fm


@app.route('/', methods=['GET', 'POST'])
def index():
    img_path = "static/images/"
    protected_img_path = "static/images/"
    if request.method == 'GET':
        img_path=None
        protected_img_path=None
    elif request.method == 'POST':
        stream = request.files['img'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)
        protected_img = fm.protect_privacy(img)

        upload_at = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        protected_img_path = img_path + upload_at + "_protected.jpg"
        img_path = img_path + upload_at + ".jpg"
        
        cv2.imwrite("flaskr/" + img_path, img)
        cv2.imwrite("flaskr/" + protected_img_path, protected_img)
        
    return render_template(
        'index.html',
        img_path=img_path,
        protected_img_path=protected_img_path
    )
