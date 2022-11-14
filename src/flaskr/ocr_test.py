import os
import time

import cv2
import easyocr
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

import image_util as iu
# import flaskr.image_util as iu


def main():
    img_path = "IMG_4670.JPG"
    img_name = os.path.splitext(img_path)[0]

    img = iu.read_image(img_path)
    ocr_results = ocr(img)
    result_img = blur(img, ocr_results)

    cv2.imwrite(f"{img_name}_ocr_result.png", result_img)


def ocr(img):
    reader = easyocr.Reader(['ja','en'])
    results = reader.readtext(img)
    if not results:
        print("文字が検出されませんでした。")

    ocr_results = []
    for result in results:
        ocr_result = {
            "points" : (
                (int(result[0][0][0]), int(result[0][0][1])),
                (int(result[0][1][0]), int(result[0][1][1])),
                (int(result[0][2][0]), int(result[0][2][1])),
                (int(result[0][3][0]), int(result[0][3][1]))
            ),
            "text"     : result[1],
            "confident": result[2]
        }
        ocr_results.append(ocr_result)
    return ocr_results


def generate_mask_image(img, ocr_results):
    mask_img = np.zeros_like(img)
    for ocr_result in ocr_results:
        cv2.fillConvexPoly(mask_img, np.array(ocr_result['points']), (255, 255, 255))
    return mask_img

def blur(img, ocr_results):
    mask_img = generate_mask_image(img, ocr_results)
    return iu.blur_image(img, mask_img)



if __name__ == "__main__":
    start_time = time.time()
    main()
    print("took:", time.time() - start_time)
