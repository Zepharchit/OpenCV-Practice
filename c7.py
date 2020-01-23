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

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('result',res)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
cap.release()