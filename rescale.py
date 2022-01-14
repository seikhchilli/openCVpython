import cv2 as cv

capture = cv.VideoCapture('video4read.mp4')

def rescale(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    frame2 = rescale(frame)

    cv.imshow("Video", frame)
    cv.imshow("VideoRescaled", frame2)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()