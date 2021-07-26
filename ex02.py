import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./images/ET.jpg',0)
cv.imshow('ET',img)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()