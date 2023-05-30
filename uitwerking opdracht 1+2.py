import numpy as np
import cv2 as cv2
import math as m
#testing if the modules are installed
print("np")
print(np.__version__)
print("cv2")
print(cv2.__version__)

#opdracht 1, image show

def test1():
        img = cv2.imread('tek1.png')
        cv2.imshow('image',img)
        k = cv2.waitKey(0)
        print(k)
        cv2.destroyAllWindows()
test1()

#opdracht 2 video capture

cap=cv2.VideoCapture(0)
while True:
        #ret means success
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(frame, gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()
