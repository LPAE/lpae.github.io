import cv2
import os
import subprocess

capture = cv2.VideoCapture(0)

ret, frame = capture.read()
cv2.imwrite("image.png", frame)
capture.release()

var = os.system("ls")
print(type(var))