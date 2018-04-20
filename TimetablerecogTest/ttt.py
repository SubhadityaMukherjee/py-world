
import numpy as np
import cv2,os
import argparse
from matplotlib import pyplot as plt

def rectify(h):
        h = h.reshape((4,2))
        hnew = np.zeros((4,2),dtype = np.float32)

        add = h.sum(1)
        hnew[0] = h[np.argmin(add)]
        hnew[2] = h[np.argmax(add)]
        
        diff = np.diff(h,axis = 1)
        hnew[1] = h[np.argmin(diff)]
        hnew[3] = h[np.argmax(diff)]
 
        return(hnew)

image = cv2.imread("imrtst.png")
#image = cv2.imread("ttable2.jpeg",1)

img = cv2.resize(image,(450,450))
col_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
col_grey=cv2.GaussianBlur(col_grey,(5,5),0)
thresh = cv2.adaptiveThreshold(col_grey,255,1,1,11,2)



_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
big = None
max_ar = 0
for a in contours:
	ar = cv2.contourArea(a)
	if(ar>100):
		peri = cv2.arcLength(a,True)
		approx = cv2.approxPolyDP(a,0.02*peri,True)
		if(ar>max_ar and len(approx)==4):
			big = approx
			max_ar = ar
#cv2.drawContours(img, contours, -1, (0,255,0), 3)

approx = rectify(approx)
h = np.array([[0,0],[449,0],[449,449],[0,449]],dtype=np.float32)
retval = cv2.getPerspectiveTransform(approx,h)
warp = cv2.warpPerspective(col_grey,retval,(450,450))
cv2.imshow("img",warp)
cv2.waitKey(0)
