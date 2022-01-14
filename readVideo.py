import cv2 as cv    #import opencv

#start video capture
capture = cv.VideoCapture('video4read.mp4')

while True:
    #reading frame by frame
    isTrue, frame = capture.read()

    #showing frame by frame
    cv.imshow('Video', frame)

    #if letter d is pressed, break 
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()