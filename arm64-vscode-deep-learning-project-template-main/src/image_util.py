from PIL import Image, ExifTags, ImageDraw, ImageFilter
import numpy as np

def read_image(file_path):
    img = Image.open(file_path)
    scale = 2000 / max(img.size)
    w = round(img.width * scale)
    h = round(img.height * scale)
    img = img.resize((w, h))
    
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = img._getexif()
        print(exif)
        if exif is not None:
            if exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
    except Exception as e:
        print(e)

    if img.mode == 'RGBA':
        img = img.convert('RGB')
    return img

def blur_image(img, positions):
    "positions: [[左上, 右上], ...]"
    blurred_image = img.filter(ImageFilter.GaussianBlur(10))

    masked_img = Image.new("L", img.size)
    draw = ImageDraw.Draw(masked_img)

    for position in positions:
        draw.rectangle([position[0], position[1]], fill=255)
        # draw.polygon(ocr_result["position"], fill=255)

    img.paste(blurred_image, (0, 0), masked_img)
    return img