import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	#hue saturation value
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	lower_green = np.array([30,0,0])
	upper_green = np.array([255,255,255])

	mask = cv2.inRange(hsv,lower_green,upper_green)
	res = cv2.bitwise_and(frame,frame,mask=mask)

	kernel = np.ones((15,15),np.float32) / 225
	smoothed = cv2.filter2D(res,-1,kernel)

	blur = cv2.GaussianBlur(res,(15,15),0)
	median = cv2.medianBlur(res,15)

	cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	cv2.imshow('result',res)
	#cv2.imshow('smooth',smoothed)
	cv2.imshow('blur',blur)
	cv2.imshow('median',median)
	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break
cv2.destroyAllWindows()
cap.release()