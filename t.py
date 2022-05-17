import cv2
capture = cv2.VideoCapture(0)

while True:
    flag,img = capture.read()
    cv2.imshow('result',img)
    if cv2.waitKey(2) == 27:
        break

capture.release()
cv2.destroyAllWindows()