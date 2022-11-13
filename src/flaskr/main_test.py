import os
import time

import flaskr.face_test as face_test
import flaskr.image_util as iu
import flaskr.ocr_test as ocr_test

IMG_PATH = "./image/test.png"

def protect_privacy(img):
    ocr_results = ocr_test.ocr(img)
    coordinates = ocr_test.set_coordinates(ocr_results)

    faces = face_test.detect_faces(img)
    coordinates.extend(face_test.set_coordinates(faces))

    # 実行速度速めのデバッグ用
    # faces = face_test.detect_faces(img)
    # coordinates = (face_test.set_coordinates(faces))

    return iu.blur_image_on_cv2(img, coordinates)


def main():
    print("start---")
    img = iu.read_image(IMG_PATH)

    ocr_results = ocr_test.ocr(img)
    coordinates = ocr_test.set_coordinates(ocr_results)

    faces = face_test.detect_faces(img)
    coordinates.extend(face_test.set_coordinates(faces))

    iu.blur_image(img, coordinates)
    
    file_name = os.path.splitext(IMG_PATH)[0]
    img.save(f"{file_name}_protect_privacy.png")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("took:", time.time() - start_time)