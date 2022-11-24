import cv2
import numpy as np
from insightface.app import FaceAnalysis


def detect_faces(img):
    if type(img) is not np.ndarray:
        raise ValueError
    app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))

    faces = app.get(img)

    if not faces:
        print("顔が検出されませんでした。")
    return faces


def generate_mask_image(img, faces):
    if type(img) is not np.ndarray or type(faces) is not list:
        raise ValueError
    mask_img = np.zeros_like(img)
    for face in faces:
        x_1, y_1, x_2, y_2 = map(int, face.bbox)
        cv2.rectangle(mask_img, (x_1, y_1), (x_2, y_2), (255, 255, 255), -1)
    return mask_img
