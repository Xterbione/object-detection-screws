import cv2 as cv
import numpy as np
#stay in while loop. awaiting keypress prevents image from being loaded
frame = cv.imread('tek3.jpg')
# Convert image from BGR to HSV+
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
lower_redL = np.array([0,50,50])
upper_redL = np.array([10,255,255])
lower_redH = np.array([170,50,50])
upper_redH = np.array([179,255,255])
lower_green = np.array([50,50,50])
upper_green = np.array([70,255,255])


# Threshold the HSV image to get only %color% colors
# all colors within the range are set to 255, all others to 0(white and black) so per pixel binary or boolean values
maskblue = cv.inRange(hsv, lower_blue, upper_blue)
maskredL = cv.inRange(hsv, lower_redL, upper_redL)
maskredH = cv.inRange(hsv, lower_redH, upper_redH)
maskgreen = cv.inRange(hsv, lower_green, upper_green)
#uses a sort of AND to check if the pixel is white in the mask
#if so, it sets the pixel to the original color, if not it'll be black
# Bitwise-AND mask and original image
resblue = cv.bitwise_and(frame,frame, mask= maskblue)
resred = cv.bitwise_and(frame,frame, mask= maskredL | maskredH)
resgreen = cv.bitwise_and(frame,frame, mask= maskgreen)
# cv.imshow('frame',frame)
# cv.imshow('mask',mask)
cv.imshow('screen1',resblue)
K = cv.waitKey(0)
print(K)
cv.destroyAllWindows()
cv.imshow('screen1',resgreen)
K = cv.waitKey(0)
print(K)
cv.destroyAllWindows()
cv.imshow('screen1',resred)
K = cv.waitKey(0)
print(K)
cv.destroyAllWindows()
#find contours
#Find contours in the mask image
#In image processing, a contour is a curve that joins all the continuous points along the boundary of an object that has the same color or intensity. 
#In other words, a contour represents the shape of an object in an image. 
contoursred, hierarchyred = cv.findContours(maskred, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(frame, contoursred, -1, (255,255,0), 3)

hull = cv.convexHull(contoursred[0])
cv.drawContours(frame, [hull], 0, (255, 255, 0), thickness=2)
#drawing the centroid:
#The centroid is the center of mass of the contour
#moments:  center of mass, area, orientation, and other statistical features.
M = cv.moments(contoursred[0])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv.circle(frame, (cx, cy), 5, (255, 255, 0), -1)
cv.imshow('screen2',frame)
K = cv.waitKey(0)
print(K)
cv.destroyAllWindows()
    