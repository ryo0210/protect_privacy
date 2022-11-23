import os
import time
import cv2

import flaskr.face_test as face_test
import flaskr.image_util as iu
import flaskr.ocr as ocr

IMG_PATH = "./image/test.png"


def protect_privacy(img):
    ocr_results = ocr.ocr(img)
    o_masked_img = ocr.generate_mask_image(img, ocr_results)

    faces = face_test.detect_faces(img)
    f_masked_img = face_test.generate_mask_image(img, faces)

    masked_img = cv2.bitwise_or(o_masked_img, f_masked_img)
    return iu.blur_image(img, masked_img)

    # 実行速度速めのデバッグ用
    # faces = face_test.detect_faces(img)
    # coordinates = (face_test.set_coordinates(faces))

    # return iu.blur_image_on_cv2(img, coordinates)


def main():
    print("start---")
    img = iu.read_image(IMG_PATH)

    ocr_results = ocr.ocr(img)
    coordinates = ocr.set_coordinates(ocr_results)

    faces = face_test.detect_faces(img)
    coordinates.extend(face_test.set_coordinates(faces))

    iu.blur_image(img, coordinates)

    file_name = os.path.splitext(IMG_PATH)[0]
    img.save(f"{file_name}_protect_privacy.png")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("took:", time.time() - start_time)
