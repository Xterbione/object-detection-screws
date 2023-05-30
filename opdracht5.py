import cv2 as cv
import numpy as np
result = []
#first we need to calculate the RIO(region of interest) for the dice
frame = cv.imread('dobbelstenen.png')
grey = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
#make image binary based on a threshold(180 in this case) 255 is color for true
ret, thresh = cv.threshold(grey, 8, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) 
hierarchy = hierarchy[0]
#cv.drawContours(frame, contours, -1, (0,255,0), 3)
#print("contours: ", len(contours))
#go over found contours, which represent the dice, we will redo detection for this
for cnr in range(len(contours)):
        cnt = contours[cnr]
        x,y,w,h = cv.boundingRect(contours[cnr])
        #cv.imshow("blurdie", blurdie)
        die = grey[y:y+h, x:x+w]
        #do something with the inner contours
        ret, thresh = cv.threshold(die, 200, 255, cv.THRESH_BINARY)
        #cv.imshow("tres", thresh)
        contours2, hierarchy2 = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        print(str(cnr) + " contours2: ", len(contours2))
        #cv.drawContours(die, contours2, -1, (0,0,0), 3)
        #cv.imshow("die", die)
        #cv.imshow('screen1',frame)
        k = cv.waitKey(0)
        cv.destroyAllWindows()
        total = 0


        #getting the inner eyes for each dice detected
        for cnr2 in range(len(contours2)):
            cnt2 = contours2[cnr2]
            area = cv.contourArea(cnt2)
            print(area)
            if area > 100:
                perimeter = cv.arcLength(cnt2, True)
                if perimeter > 0:
                    vormfactor = 4 * np.pi * area / perimeter ** 2
                    print(vormfactor)
                    if vormfactor > 0.50:
                        total = total + 1
                    #hyrarchie is een lijst met lijsten. de eerste lijst bevat de volgende lijsten()
                    #child = hierarchy[cnr2][2]
                    #print("dice: ",cnr ,"area: ",area, "vormfactor: ", vormfactor)
                    #print(cv.HoughCircles(grey, cv.HOUGH_GRADIENT, 1, 80,
                    #             param1=50, param2=30, minRadius=10, maxRadius=0))
                    #if area > 1.5:
                    #    total = total + 1
        result.append(total) 
result.sort()     
#cv.imshow('screen1',frame)
k = cv.waitKey(0)
cv.destroyAllWindows()
#print("total dices: ",len(result))
print(result)
    