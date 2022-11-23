from flaskr.ocr import ocr
# from ocr import ocr
import pytest


def test_ocr_raise():
    img = "/test.png"
    with pytest.raises(ValueError):
        ocr(img)


if __name__ == "__main__":
    test_ocr_raise()
