import time

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def openpic(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)

    hierarchy, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    lstin = []
    for i in contours:
        peri = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.04 * peri, True)
        cv2.drawContours(img, approx, -1, color=(0, 255, 0), thickness=-3)
    cv2.imshow("output", img)
    cv2.waitKey(0)

def findgrid(img):
    cells = []
    #NO OF ROWS = 16, NO COLMS = 11
    H, W,D = img.shape
    cell_width = 130
    cell_height = 114
    print(img.shape,cell_height,cell_width)
    for r in range(0, W, cell_width):
        row = []
        for c in range(0, H, cell_height):
            cell = img[r:r + cell_width, c:c + cell_height]
            if((118,249,224) in cell):
                row.append(1)
            else:
                row.append(0)
        cells.append(row)
    f = open("oput.txt","w")
    f.write(str(cells))
    print(cells,len(cells[0]),len(cells))

def colorpic(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    boundaries = [([74, 100, 100], [94, 255, 255])]
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(img, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)
        cv2.imwrite("test.jpeg",output)
        return (output)
        break


img = cv2.imread("ttable2.jpeg", 1)
cv2.resize(img,(300,300))
print(img.shape)
findgrid(colorpic(img))