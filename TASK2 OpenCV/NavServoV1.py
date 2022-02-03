import time
import cv2
import numpy as np
import math
import RPi.GPIO as gpio
from picamera.array import PiRGBArray
from picamera import PiCamera

start = time.time()
'''camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))'''
# allow the camera to warmup
time.sleep(0.1)
print("Camera Initialized")
a = input("Enter colour of the landing zone : ")
# capture frames from the camera
#*********NOTE*********
# USING 135 AS UP AND 45 AS DOWN POSITION
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(35, gpio.OUT)
gpio.setup(33, gpio.OUT)
lpwm = gpio.PWM(35, 50)
rpwm = gpio.PWM(33, 50)
lpwm.start(0)
rpwm.start(0)
print('Initializing Pins ... and waiting for 2 sec')
print('waiting for 2 seconds')
#lpwm.ChangeDutyCycle(1.5)
#rpwm.ChangeDutyCycle(1.5)
time.sleep(2)
Xposition = 90
Yposition = 90
print(f"Initialized home positions of left servo as {Xposition} and right servo as {Yposition}")


def top_move(Xposition, Yposition):
    # Xposition += 10  # LEFT SERVO
    # ser.write((str(Xposition) + 'a').encode('utf-8'))
    i=135
    position = 1. / 18. * (i) + 2
    lpwm.ChangeDutyCycle(position)
    rpwm.ChangeDutyCycle(position)
    Yposition += 10  # RIGHT SERVO
    # ser.write((str(Yposition) + 'a').encode('utf-8'))
    time.sleep(0.03)
    print('Going Up ...')
    # ///////////////////////////////////////


def down_move(Xposition, Yposition):
    # for going DOWN assuming medium x as left servo and medium y as right
    i = 45
    position = 1. / 18. * (i) + 2
    lpwm.ChangeDutyCycle(position)
    rpwm.ChangeDutyCycle(position)
    Xposition -= 10  # LEFT SERVO
    # ser.write((str(Xposition) + 'a').encode('utf-8'))
    # time.sleep(0.03)
    Yposition -= 10  # RIGHT SERVO
    # ser.write((str(Yposition) + 'a').encode('utf-8'))
    time.sleep(0.03)
    print('Going Down ...')


def left_move(Xposition, Yposition):
    # for going LEFT assuming medium x as left servo and medium y as right
    Xposition -= 10  # LEFT SERVO
    i = 45
    j=135
    position = 1. / 18. * (i) + 2
    position2 = 1. / 18. * (j) + 2
    lpwm.ChangeDutyCycle(position2)
    rpwm.ChangeDutyCycle(position)
    # ser.write((str(Xposition) + 'a').encode('utf-8'))
    # time.sleep(0.03)
    Yposition += 10  # RIGHT SERVO
    # ser.write((str(Yposition) + 'a').encode('utf-8'))
    time.sleep(0.03)
    print('Going Left ...')


# for going RIGHT assuming medium x as left servo and medium y as right
def right_move(Xposition, Yposition):
    Xposition += 10  # LEFT SERVO
    i = 135
    j = 45
    position = 1. / 18. * (i) + 2
    position2 = 1. / 18. * (j) + 2
    lpwm.ChangeDutyCycle(position2)
    rpwm.ChangeDutyCycle(position)
    # ser.write((str(Xposition) + 'a').encode('utf-8'))
    # time.sleep(0.03)
    Yposition -= 10  # RIGHT SERVO
    # ser.write((str(Yposition) + 'a').encode('utf-8'))
    print('Going Right ...')
    time.sleep(0.03)


if (a == 'red'):
    # lower_red = np.array([160, 50, 50])
    # upper_red = np.array([180, 255, 255])
    red_lower = np.array([107, 99, 101], np.uint8)
    red_upper = np.array([179, 255, 255], np.uint8)
#         lower_red = np.array([0, 50, 20])
#         upper_red = np.array([5, 255, 255])
elif (a == 'orange'):
    lower_red = np.array([7, 128, 140])
    upper_red = np.array([27, 255, 255])
elif (a == 'yellow'):
    # lower_red = np.array([20, 100, 100])
    # upper_red = np.array([30, 255, 255])
    lower_red = np.array([22, 146, 18])
    upper_red = np.array([53, 255, 255])
elif (a == 'white'):
    lower_red = np.array([0, 0, 255])
    upper_red = np.array([255, 255, 255])
elif (a == 'orange'):
    lower_red = np.array([20, 100, 100])
    upper_red = np.array([30, 255, 255])
elif (a == 'blue'):
    # lower_red = np.array([20, 100, 100])
    # upper_red = np.array([30, 255, 255])
    lower_red = np.array([107, 99, 101])
    upper_red = np.array([179, 255, 255])
else:
    print('Check colour and retry')
    sys.exit(0)
cap = cv2.VideoCapture(1)

print(
    f'Starting the main loop ... Camera Ready and hsv colours initialized ...\nExecution time taken tilll now {time.time() - start} sec')
#for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
while True:
    _,frame=cap.read()
    #frame = frame.array
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))
    blur = cv2.GaussianBlur(frame, (5, 5), 20)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # red_lower = np.array([0, 50, 20], np.uint8)
    # red_upper = np.array([5, 255, 255], np.uint8)
    # red_lower = np.array([22, 146, 18], np.uint8)
    # red_upper = np.array([53, 255, 255], np.uint8)
    output = frame.copy()
    mask = cv2.inRange(hsv, red_lower, red_upper)
    kernel = np.ones((2, 3), np.uint8)
    gray = cv2.erode(mask, kernel, iterations=1)
    # gray = erosion

    gray = cv2.dilate(gray, kernel, iterations=1)
    # detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=1000)
    # print circles

    # ensure at least some circles were found
    #print('Starting the circle detection algorithm ...')
    if circles is not None and ():
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle in the image
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            r = str(r)
            diameter = 2 * r
            a = f'Radius is {r}'
            b = f'Center is ({x},{y})'
            red_circle = cv2.putText(output, b, (x - 5 + 80, y - 5 + 120), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                                     (255, 255, 255), 4)
            print(red_circle)
            cv2.putText(output, a, (x - 5 + 10, y - 5 + 60), cv2.FONT_HERSHEY_COMPLEX, 0.7, (100, 255, 255), 4)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    rows, cols, _ = frame.shape
    center_x = int(rows / 2)
    center_y = int(cols / 2)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "x = " + str(x) + "y = " + str(y)
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255))
        '''gamma = 0.8423
        altitude = 0.20
        a = 0
        txsx = x + (w / 0.5)
        cxsx = 300
        # b = math.degrees(math.atan((math.degrees(tan(gamma/2))(txsx))/cxsx)
        b = math.degrees(math.atan(math.degrees(math.tan(gamma / 2)) * txsx / cxsx))
        dis = altitude * math.degrees(math.tan(a + b))
        print(b)
        print(dis)
        dis=str(dis)
        cv2.putText(frame, dis, (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 50))'''
        medium_x = int((x + x + w) / 2)
        medium_y = int((y + y + h) / 2)

        cv2.line(frame, (medium_x, 0), (medium_x, 600), (0, 255, 0), 2)
        text2 = "mediumX = " + str(medium_x)
        cv2.putText(frame, text2, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 50))
        # ////////////////////////////////////////////////////////////////////
        cv2.line(frame, (0, medium_y), (600, medium_y), (0, 255, 0), 2)
        text3 = "mediumY = " + str(medium_y)
        cv2.putText(frame, text3, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 50))
        #         Navigation code from Navigation.py
        print('Starting Navigation Algorithm ...')
        # ///////////////////////////////////////////////////////////////
        if medium_x > int(frame.shape[1] / 2) and medium_y > int(frame.shape[0] / 2) and medium_x > int(frame.shape[1] / 2) + 30 and medium_y > int(
                frame.shape[0] / 2) + 30 and medium_x < int(frame.shape[1] / 2) + 100 and medium_y < int(frame.shape[0] / 2) + 100:
            #cv2.putText(frame, "Circle is towards bottom right!!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),
                        #2)
            right_move(Xposition, Yposition)
        # elif x > int(frame.shape[1] / 2) and y > int(frame.shape[0] / 2) and x > int(frame.shape[1] / 2) + 100 and y > int(frame.shape[0] / 2) + 100:
        #     cv2.putText(img, "Circle is towards extreme bottom right!!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),2)
        elif medium_x < int(frame.shape[1] / 2) and medium_y > int(frame.shape[0] / 2) and medium_x < int(
                frame.shape[1] / 2) + 30 and medium_y > int(frame.shape[0] / 2) + 30 and medium_x < int(
                frame.shape[1] / 2) + 35 and medium_y > int(frame.shape[0] / 2) + 30:
            #cv2.putText(frame, "Circle is towards bottom left !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),
                        #2)
            left_move(Xposition, Yposition)
        # elif x<int(frame.shape[1] / 2) and y>int(frame.shape[0] / 2) and x<int(frame.shape[1] / 2)+35 and y>int(frame.shape[0]/2)+35:
        #     cv2.putText(img, "Circle is towards extreme bottom left !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        elif medium_x < int(frame.shape[1] / 2) and medium_y < int(frame.shape[0] / 2) and medium_x < int(
                frame.shape[1] / 2) + 30 and medium_y < int(frame.shape[0] / 2) + 30:
            cv2.putText(frame, "Circle is towards top left !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            left_move(Xposition, Yposition)
            #left_move(Xposition, Yposition)
        # elif x<int(frame.shape[1] / 2) and y<int(frame.shape[0] / 2)and x<int(frame.shape[1] / 2)+35 and y<int(frame.shape[0]/2)+35:
        #     cv2.putText(img, "Circle is towards extreme top left !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        elif medium_x > int(frame.shape[1] / 2) and medium_y < int(frame.shape[0] / 2) and medium_x > int(
                frame.shape[1] / 2) + 30 and medium_y < int(frame.shape[0] / 2) + 30:
           # cv2.putText(frame, "Circle is towards top right !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            right_move(Xposition, Yposition)
        # elif x>int(frame.shape[1] / 2) and y<int(frame.shape[0] / 2)and x>int(frame.shape[1] / 2)+35 and y<int(frame.shape[0]/2)+35:
        #     cv2.putText(img, "Circle is towards extreme top right !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        elif medium_x != 0:
            cv2.putText(frame, "Circle is right in front !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    # ////////////////////////////////////////////////////////////////
    #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    #cv2.putText(mask, f"FPS \n {fps}", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #stacked = np.hstack((mask, frame))
    cv2.imshow('frame',frame)
    #cv2.imshow('GUI OP !!!', cv2.resize(stacked, None, fx=1, fy=1))
    key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# end = time.time()
# print(f'Total Execution Time {end - start} seconds')
cv2.destroyAllWindows()
