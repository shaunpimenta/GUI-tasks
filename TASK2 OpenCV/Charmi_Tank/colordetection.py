import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Red color

    lower_red=np.array([161,155,84])
    higher_red=np.array([179,255,255])
    red_mask =cv2.inRange(hsv_frame,lower_red,higher_red)
    red=cv2.bitwise_and(frame,frame,mask=red_mask)
    #blue color

    lower_blue=np.array([94,80,21])
    high_blue=np.array([126,255,255])
    blue_mask=cv2.inRange(hsv_frame,lower_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    #green color

    lower_green= np.array([25, 52, 72])
    high_green = np.array([102,255 , 255])
    green_mask = cv2.inRange(hsv_frame, lower_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow("Frame",frame)  #for showing all we have used imshow
    cv2.imshow("Red mask", red)
    cv2.imshow("blue mask", blue)
    cv2.imshow("green mask", green)

    key=cv2.waitKey(1)
    if key == 27:
        break
