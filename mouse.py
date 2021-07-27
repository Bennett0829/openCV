import cv2

def drawcircle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),3)

img = cv2.imread('./images/ET.jpg')

cv2.namedWindow('imge',cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image',drawcircle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()