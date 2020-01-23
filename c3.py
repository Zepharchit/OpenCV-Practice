import cv2
import numpy as np

img =  cv2.imread('./abx.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(0,224,224),15)
cv2.rectangle(img,(15,25),(200,150),(140,120,0),10)
cv2.circle(img,(100,65),55,(90,120,220),-1)


pts = np.array([[100,125],[420,370],[327,520],[550,110]],np.int32)
#pts = pts.reshape((-1,1,2))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Opencv',(0,240),font,3,(200,255,255),2,cv2.LINE_AA)
cv2.polylines(img,[pts],True,(0,255,255),3)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows( )