import pytest

import flaskr.image_util as iu
import flaskr.ocr as ocr


def test_ocr_raise():
    img = "not_exist.png"
    with pytest.raises(ValueError):
        ocr.ocr(img)


def test_ocr_no_text():
    img = iu.read_image("black.png")
    ocr_results = ocr.ocr(img)
    assert ocr_results == []


def test_generate_mask_image_shape():
    img = iu.read_image("test_small.jpg")
    ocr_results = []
    mask_img = ocr.generate_mask_image(img, ocr_results)
    assert mask_img.shape == img.shape
