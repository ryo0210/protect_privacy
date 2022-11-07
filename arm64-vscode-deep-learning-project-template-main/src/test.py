import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

img = cv2.imread("src.png")
# img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

faces = app.get(img)
rimg = app.draw_on(img, faces)

x_1, y_1, x_2, y_2 = map(int, faces[0].bbox)
w = x_2 - x_1
h = y_2 - y_1

result = img.copy()
bbox = cv2.rectangle(result, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)
result = mosaic_area(img, x_1, y_1, w, h)

cv2.imwrite("./t1_output.jpg", rimg)
cv2.imwrite("./bbox.jpg", bbox)
cv2.imwrite("./mosaic_result.jpg", result)
# cv2.imshow("test", rimg)
# cv2.waitKey(0)


