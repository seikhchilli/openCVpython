#import opencv
import cv2 as cv

#imread() is used to read an image and convert into a matrix
img = cv.imread('img4read.jpg')

#imshow() is used to show thw image
cv.imshow('name of window', img)


#when passed 0, it waits for infite amount of time until keyboard key is preses
cv.waitKey(0)