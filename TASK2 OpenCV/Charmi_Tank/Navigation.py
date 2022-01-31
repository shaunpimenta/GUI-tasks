import serial
import time
import cv2
import numpy as np
import PCA9685
import RPi.GPIO as gpio
# initialize the camera and grab a reference to the raw camera capture
# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 32
# rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)


# PCA9685 = PCA9685.PCA9685
# pwm = PCA9685(0x40, debug=False)
# pwm.setPWMFreq(50)

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(35, gpio.OUT)
gpio.setip(33, gpio.OUT)
lpwm = gpio.PWM(35, 50)
# rpwm = gpio.PWM(35, 50)
# pwm.start(0)
print('waiting for 2 seconds')
time.sleep(2)

cap = cv2.VideoCapture(0)
medium_x=0
medium_y=0

X_MAX = 2500.0
X_MIN = 500.0
X_HOME = 1500.0

Y_MAX = 2500.0
Y_MIN = 500.0
Y_HOME = 1500.0

W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
print('W,H,fps: ', W , H , fps)

def move(x_move, y_move):
    lpwm.setServoPulse(0,x_move)
    lpwm.setServoPulse(1,y_move)

move(X_HOME, Y_HOME)


now_degree_x, now_degree_y, move_degree_x, move_degree_y = X_HOME, Y_HOME, 0, 0





Xposition = 90
Yposition = 90

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (300, 300))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_lower = np.array([161, 155, 84], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    mask = cv2.inRange(hsv, red_lower, red_upper)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    mask = cv2.medianBlur(mask, 5)
    output = frame.copy()
    kernel = np.ones((2, 3), np.uint8)
    gray = cv2.erode(mask, kernel, iterations=1)
    # gray = erosion

    gray = cv2.dilate(gray, kernel, iterations=1)
    # gray = dilation

    # get the size of the final image
    # img_size = gray.shape
    # print img_size

    # detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=1000)
    # print circles
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    rows, cols, _ = frame.shape
    center_x = int(rows / 2)
    center_y = int(cols / 2)
#new

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle in the image
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            # cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "x = " + str(x) + "y = " + str(y)
                cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255))

                medium_x = int((x + x + w) / 2)
                medium_y = int((y + y + h) / 2)

                # 640,480
                move_degree_x = now_degree_x - (x_medium - 320) * 0.3
                move_degree_y = now_degree_y - (y_medium - 240) * 0.3

                if move_degree_x > X_MIN and move_degree_x < X_MAX:
                    if move_degree_y > Y_MIN and move_degree_y < Y_MAX:
                        move(move_degree_x, move_degree_y)
                        now_degree_x = move_degree_x
                        now_degree_y = move_degree_y

                cv2.line(frame, (medium_x, 0), (medium_x, 480), (0, 255, 0), 2)
                text2 = "mediumX = " + str(medium_x)
                cv2.putText(frame, text2, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 50))
                # ////////////////////////////////////////////////////////////////////
                cv2.line(frame, (0, medium_y), (640, medium_y), (0, 255, 0), 2)
                text3 = "mediumY = " + str(medium_y)
                cv2.putText(frame, text3, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 50))


















                break

            r = str(r)
            diameter = 2 * r
            a = f'Radius is {r}'
            b = f'Center is ({x},{y})'
            cv2.putText(output, b, (x - 5 + 80, y - 5 + 120), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (255, 255, 255), 4)
            cv2.putText(output, a, (x - 5 + 10, y - 5 + 60), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (100, 255, 255), 4)
            # time.sleep(0.5)
            # print("Column Number: ")
            # print(x)
            # print("Row Number: ")
            # print(y)
            # print("Radius is: ")
            # print(r)
            print(f"Center is ({x},{y})")
    # end


    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask )
    key = cv2.waitKey(1)
    if key ==27:
        break
cap.release()
cv2.destroyAllWindows()





