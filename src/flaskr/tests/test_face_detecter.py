import pytest

import flaskr.image_util as iu
import flaskr.face_detecter as fd


def test_detect_face_raise():
    img = "not_exist.png"
    with pytest.raises(ValueError):
        fd.detect_faces(img)


def test_detect_face_no_face():
    img = iu.read_image("./flaskr/tests/black.png")
    ocr_results = fd.detect_faces(img)
    assert ocr_results == []


def test_generate_mask_image_shape():
    img = iu.read_image("./flaskr/tests/test_small.jpg")
    faces = []
    mask_img = fd.generate_mask_image(img, faces)
    assert mask_img.shape == img.shape
