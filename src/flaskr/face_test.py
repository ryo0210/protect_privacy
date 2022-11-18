import os
import time

import cv2
import numpy as np
from insightface.app import FaceAnalysis

import flaskr.image_util as iu


def main():
    # img_path = "./image/face/nearby_face.jpg"
    img_path = "./image/IMG_4656.JPG"
    img_name = os.path.splitext(img_path)[0]

    img = iu.read_image(img_path)
    faces = detect_faces(img)
    result_img = blur_image(img, faces)

    result_img.save(f"{img_name}_face_result.png")


def detect_faces(img):
    app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))

    faces = app.get(np.array(img))

    if not faces:
        print("顔が検出されませんでした。")
    return faces


def set_coordinates(faces):
    coordinates = []
    for face in faces:
        x_1, y_1, x_2, y_2 = map(int, face.bbox)
        coordinates.append([(x_1, y_1), (x_2, y_2)])
    return coordinates


def generate_mask_image(img, faces):
    mask_img = np.zeros_like(img)
    for face in faces:
        x_1, y_1, x_2, y_2 = map(int, face.bbox)
        cv2.rectangle(mask_img, (x_1, y_1), (x_2, y_2), (255, 255, 255), -1)
    return mask_img


def blur_image(img, faces):
    coordinates = set_coordinates(faces)
    return iu.blur_image(img, coordinates)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("took:", time.time() - start_time)
