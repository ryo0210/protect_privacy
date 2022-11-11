import os
import time

import cv2
import easyocr
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

import image_util as iu


def main():
    img_path = "./image/word/IMG_4646.JPG"
    # img_path = "./image/scenery.jpg"
    img_name = os.path.splitext(img_path)[0]

    img = iu.read_image(img_path)
    ocr_results = ocr(img)
    result_img = blur_image(img, ocr_results)

    result_img.save(f"{img_name}_ocr_result.png")


def ocr(img):
    reader = easyocr.Reader(['ja','en'])
    results = reader.readtext(np.array(img))
    if not results:
        print("文字が検出されませんでした。")

    ocr_results = []
    for result in results:
        ocr_result = {
            "position" : (
                (int(result[0][0][0]), int(result[0][0][1])),
                (int(result[0][1][0]), int(result[0][1][1])),
                (int(result[0][2][0]), int(result[0][2][1])),
                (int(result[0][3][0]), int(result[0][3][1]))
            ),
            "text"     : result[1],
            "confident": result[2]
        }
        print(ocr_result)
        ocr_results.append(ocr_result)
    return ocr_results

def set_coordinates(ocr_results):
    coordinates = []
    for ocr_result in ocr_results:
        coordinates.append([ocr_result["position"][0], ocr_result["position"][2]])
    return coordinates


def blur_image(img, ocr_results):
    coordinates = set_coordinates(ocr_results)
    return iu.blur_image(img, coordinates)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("took:", time.time() - start_time)
