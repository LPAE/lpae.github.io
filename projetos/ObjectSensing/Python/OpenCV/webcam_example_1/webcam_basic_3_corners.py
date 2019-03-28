import cv2
import numpy as np

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(1)

while 1:
    ret, frame = capture.read()

    frame = cv2.resize(frame, None, fx=5, fy=5, interpolation=cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)

    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    frame[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imshow('frame', frame)

    # ------------------------------------------------------------------------------------------------------------------
    # Esc -> EXIT while
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # ------------------------------------------------------------------------------------------------------------------

capture.release()
cv2.destroyAllWindows()
