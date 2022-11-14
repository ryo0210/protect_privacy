from PIL import Image, ExifTags, ImageDraw, ImageFilter
import numpy as np
import cv2

def read_image(file_path):
    img = Image.open(file_path)
    # scale = 1080 / max(img.size)
    # w = round(img.width * scale)
    # h = round(img.height * scale)
    # img = img.resize((w, h))
    
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = img._getexif()
        if exif is not None:
            if exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
    except Exception as e:
        print(e)

    return pil2cv(img)

def pil2cv(img):
    mode = img.mode
    if mode == '1':
        return np.array(img, dtype=np.uint8) * 255
        # return cv_img
    elif mode == 'RGB':
        cv_img = np.array(img, dtype=np.uint8)
        return cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    elif mode == 'P' or mode == 'CMYK':
        cv_img = np.array(img.convert('RGB'), dtype=np.uint8)
        return cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    elif mode == 'RGBA':
        cv_img = np.array(img, dtype=np.uint8)
        return cv2.cvtColor(cv_img, cv2.COLOR_RGBA2BGR)
    else:
        raise ValueError(f'unhandled image color mode: {mode}')


def blur_image(src, mask_img):
    blurred_image = cv2.GaussianBlur(src, (99, 99), 0)
    transparency = (0, 0, 0)
    front = cv2.bitwise_and(blurred_image, mask_img)
    return np.where(front==transparency, src, front)
    