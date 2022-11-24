import cv2

import flaskr.face_detecter as fd
import flaskr.image_util as iu
import flaskr.ocr as ocr


def protect_privacy(img):
    ocr_results = ocr.ocr(img)
    o_masked_img = ocr.generate_mask_image(img, ocr_results)

    faces = fd.detect_faces(img)
    f_masked_img = fd.generate_mask_image(img, faces)

    masked_img = cv2.bitwise_or(o_masked_img, f_masked_img)
    return iu.blur_image(img, masked_img)
