import cv2 as cv
import numpy as np
#stay in while loop. awaiting keypress prevents image from being loaded
frame = cv.imread('bouten_moeren1.jpg')
grey = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
greyblur = cv.GaussianBlur(grey,(5,5),0)
#make image binary based on a threshold(180 in this case) 255 is color for true
retention,threshold = cv.threshold(greyblur, 180, 255,cv.THRESH_BINARY_INV)
contours, hierarchy = cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) 
#[Next, Previous, First_Child, Parent]
hierarchy = hierarchy[0]
#cv.drawContours(frame, contours, -1, (255,255,0), 3)
for cnr in range(len(contours)):
    cnt = contours[cnr]
    area = cv.contourArea(cnt)
    holes = 0
    if cv.arcLength(cnt, True) > 0:
     vormfactor = 4 * np.pi * area / cv.arcLength(cnt, True) ** 2
    #hyrarchie is een lijst met lijsten. de eerste lijst bevat de volgende lijsten()
    #get child index, if no child -1
    child = hierarchy[cnr][2]
    while child >= 0:
        #oppervlakte van child
        holes += cv.contourArea(contours[child])
        #get child index, if no child -1
        child = hierarchy[child][0]
        print("hole:", "area: ",area, "vormfactor: ", vormfactor,"holes:", holes)
        # teken alleen contouren met een oppervlakte groter dan 100, en andere thresholds
        # screw: 255,0,0 nut: 0,255,0  wrong: 0,0,255
        # formvactor is circular number
        # holes is amount of children objects inside object
        # area is surface area
    if area > 500 and vormfactor < 0.89:
        if vormfactor > 0.8:
            if holes > 150:
                cv.drawContours(frame, [cnt], -1, (0,255,0), 3)
            else:
                cv.drawContours(frame, [cnt], -1, (255,50,0), 3)
        else:
            if area > 2230:
                cv.drawContours(frame, [cnt], -1, (215,0,50), 3)
            else:
                cv.drawContours(frame, [cnt], -1, (50,135,0), 3)                  
cv.imshow('screen1',frame)
k = cv.waitKey(0)
print("k: ",k)
    