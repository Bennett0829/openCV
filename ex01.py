import cv2

#開圖
img1 = cv2.imread('./images/ET.jpg')

#秀圖
cv2.imshow('ET',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()