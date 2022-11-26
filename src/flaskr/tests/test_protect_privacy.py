import flaskr.image_util as iu
from flaskr.protect_privacy import protect_privacy


def test_protect_privacy_no_():
    img = iu.read_image("./flaskr/tests/black.png")
    protected_img = protect_privacy(img)
    assert protected_img.shape == img.shape
