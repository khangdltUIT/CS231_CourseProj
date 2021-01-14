import cv2
import numpy as np
import sys

def color_quantization(img, k):
# Defining input data for clustering
  data = np.float32(img).reshape((-1, 3))
# Defining criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
# Applying cv2.kmeans function
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result


img = cv2.imread(sys.argv[1])

edges = cv2.Canny(img, 100, 200)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_1 = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray_1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)

color = cv2.bilateralFilter(img, d=9, sigmaColor=200,sigmaSpace=200)

cartoon = cv2.bitwise_and(color, color, mask=edges)

img_1 = color_quantization(img, 7)

blurred = cv2.medianBlur(img_1, 3)
#cv2.imshow(blurred)

cartoon_1 = cv2.bitwise_and(blurred, blurred, mask=edges)
cv2.imshow("Quanti cartoon",cartoon_1)

cv2.waitKey(0)
cv2.destroyAllWindows()