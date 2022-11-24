import base64

import cv2
import numpy as np
from flask import render_template, request

from flaskr.protect_privacy import protect_privacy
from flaskr import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template(
            'index.html'
        )
    if request.method == 'POST':
        try:
            img = read_image(request)
        except cv2.error:
            return render_template(
                'index.html',
                message=f"{request.files['img'].filename}は対応していないファイルです。"
            )

        protected_img = protect_privacy(img)

        return render_template(
            'index.html',
            file_name=request.files['img'].filename.split(".")[0],
            base64_img=cv_to_base64(img),
            protected_base64_img=cv_to_base64(protected_img),
        )


def read_image(request):
    stream = request.files['img'].stream
    img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, 1)


def cv_to_base64(img):
    _, encoded = cv2.imencode(".jpg", img)
    return base64.b64encode(encoded).decode("ascii")
