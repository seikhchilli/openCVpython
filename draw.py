import cv2 as cv
import numpy as np

#creating an array of zeros with datatype of uint8 used for images
blank = np.zeros((500, 500, 3), dtype = 'uint8')
#show blank image
cv.imshow('blank', blank)

#1.drawing image of particular color

#blank[:] = 0, 255, 0

#cv.imshow('green', blank)

#2.drawing a rectangle

#cv.rectangle(image, vertex1, vertex4, color, thickness)
#thickness = cv.FILLED for recatngle to be filled, or thickness = -1
cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness = 2)
cv.imshow('Rectangle', blank)

#3.drawing a circle

#cv.circle(image, center of circle, radius in pixels, color, thickness)
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness = 3)
cv.imshow('Circle', blank)

#4.drawing a line

#cv.line(image, from, to, color, thickness)
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness = 3)
cv.imshow('Line', blank)

cv.waitKey(0)
