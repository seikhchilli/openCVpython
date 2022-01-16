import cv2 as cv

img = cv.imread('img4read.jpg')

cv.imshow("image", img)

#1. converting to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow("gray_image", grayscale_img)

#2. blur the image

#cv.GaussianBlur(image, kernel size, cv.BORDER_DEFAULT)
#increase kernel size to increase blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("blurred image", blur)

#3. Edge cascade

#cv.Canny(image, threshold1, threshold2)
canny = cv.Canny(img, 125, 175)
cv.imshow("canny edges", canny)

#4. Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations = 1)
cv.imshow("dilated", dilated)

cv.waitKey(0)