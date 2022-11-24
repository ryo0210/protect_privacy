import cv2
import easyocr
import numpy as np


PRIVACY_KEYWORD = ['様', '住所', 'TEL', 'FAX']
PRIVACY_NUMBER = ['〒', 'テ', '番号', 'ID']
PRIVACY_TEXT = PRIVACY_KEYWORD + PRIVACY_NUMBER


def ocr(img):
    if type(img) is not np.ndarray:
        raise ValueError
    reader = easyocr.Reader(['ja', 'en'])
    results = reader.readtext(img)
    if not results:
        print("文字が検出されませんでした。")

    ocr_results = []
    for result in results:
        ocr_result = {
            "points": (
                (int(result[0][0][0]), int(result[0][0][1])),
                (int(result[0][1][0]), int(result[0][1][1])),
                (int(result[0][2][0]), int(result[0][2][1])),
                (int(result[0][3][0]), int(result[0][3][1]))
            ),
            "text": result[1],
            "confident": result[2]
        }
        print(ocr_result)
        ocr_results.append(ocr_result)
    return ocr_results


def generate_mask_image(img, ocr_results):
    if type(img) is not np.ndarray:
        raise ValueError
    mask_img = np.zeros_like(img)
    for ocr_result in ocr_results:
        cv2.fillConvexPoly(mask_img, np.array(ocr_result['points']), (255, 255, 255))
    return mask_img

    # mask_privacy_img = np.zeros_like(img)
    # for ocr_result in ocr_results:
    #     if contains_privacy(ocr_result['text']):
    #         print(ocr_result['text'])
    #         cv2.fillConvexPoly(mask_privacy_img, np.array(ocr_result['points']), (255, 255, 255))
    # return mask_privacy_img


def contains_privacy(text):
    for privacy_text in PRIVACY_TEXT:
        if privacy_text in text:
            return True
    return False

    # return PRIVACY_TEXT in text
