import easyocr
import cv2
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

reader = easyocr.Reader(['en','ja'], gpu=False) # this needs to run only once to load the model into memory
img = cv2.imread("src_ocr.jpeg")
# img = cv2.resize(img, None, fx=0.3, fy=0.3)
# cv2.imwrite("./small_img.jpg", img)

result = reader.readtext(img)
print(result)

result_img = img.copy()
for s in result:
    print(s[0][0][0], s[0][0][1], s[0][1][0], s[0][1][1])
    cv2.rectangle(result_img, (int(s[0][0][0]), int(s[0][0][1])), (int(s[0][2][0]), int(s[0][2][1])), (0, 255, 0), 2)
    print(s[1])


print("result")
print(result)
cv2.imwrite("./ocr_result_img.jpg", result_img)
