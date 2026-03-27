import pytesseract
import cv2
import time
from matplotlib import pyplot as plt

imagePath = "image.png"
image = cv2.imread(imagePath)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(pytesseract.image_to_string(imagePath))