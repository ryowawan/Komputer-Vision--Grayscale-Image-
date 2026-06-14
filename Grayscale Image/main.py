# 1. Import pustaka
import cv2 as cv
# 2. 
img = cv.imread("...")
#
from google.colab.patches import cv2_imshow
cv2_imshow(img)
# 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv2_imshow(gray)
