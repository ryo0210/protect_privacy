import base64

import cv2
import numpy as np
from flask import render_template, request

import flaskr.main_test as fm
from flaskr import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        base64_img = None
        protected_base64_img = None
    elif request.method == 'POST':
        img = read_image(request)

        protected_img = fm.protect_privacy(img)

        base64_img = cv_to_base64(img)
        protected_base64_img = cv_to_base64(protected_img)

    return render_template(
        'index.html',
        base64_img=base64_img,
        protected_base64_img=protected_base64_img
    )


def read_image(request):
    stream = request.files['img'].stream
    img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, 1)


def cv_to_base64(img):
    _, encoded = cv2.imencode(".jpg", img)
    return base64.b64encode(encoded).decode("ascii")
