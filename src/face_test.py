import os
import sys
import time

import cv2
import insightface
import numpy as np
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

import image_util as iu

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
    # rimg = app.draw_on(img, faces)

    if not faces:
        print("顔が検出されませんでした。")
    return faces

def set_coordinates(faces):
    coordinates = []
    for face in faces:
        x_1, y_1, x_2, y_2 = map(int, face.bbox)
        coordinates.append([(x_1, y_1), (x_2, y_2)])
    return coordinates

def blur_image(img, faces):
    coordinates = set_coordinates(faces)
    return iu.blur_image(img, coordinates)


# def mosaic_area(src, x, y, width, height, ratio=0.1):
#     dst = src.copy()
#     dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
#     return dst

# def mosaic(src, ratio=0.1):
#     small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
#     return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("took:", time.time() - start_time)


