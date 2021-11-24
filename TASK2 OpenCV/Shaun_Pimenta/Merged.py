import cv2
# import CircleDetection as circle
import numpy as np
a = str(input("Enter circle color"))
cap = cv2.VideoCapture(0)


# tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.legacy.TrackerCSRT_create()
success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)
def drawBox(img, bbox,frame):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    y1=int(y+(h/2))
    x1=int(x+(w/2))
    print(x1)
    print(y1)
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)
    # cv2.line(img, (x+int(w/2), 0), (x+int(w/2), y2), (0, 255, 0), thickness=line_thickness)
    cv2.line(frame, (x1, y1), (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), (0, 255, 0), thickness=5)
    cv2.line(img, (x1,y1), (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), (0, 255, 0), thickness=5)
    dis = ((x - int(frame.shape[1] / 2)) ** 2 - (y - int(frame.shape[0] / 2))) ** 0.5
    print(f'Distance is {dis}')
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

    return w

while (1):

    timer = cv2.getTickCount()
    # img = circle.CircleDetection(a)
    _, frame = cap.read()
    # cv2.imshow('OP',frame)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # # define range of red color in HSV
    if (a == 'red'):
        # lower_red = np.array([160, 50, 50])
        # upper_red = np.array([180, 255, 255])
        lower_red = np.array([0, 50, 20])
        upper_red = np.array([5, 255, 255])
    elif (a == 'green'):
        lower_red = np.array([50, 100, 100])
        upper_red = np.array([70, 255, 255])
    elif (a == 'yellow'):
        lower_red = np.array([20, 100, 100])
        upper_red = np.array([30, 255, 255])
    elif (a == 'white'):
        lower_red = np.array([0, 0, 255])
        upper_red = np.array([255, 255, 255])
    elif (a == 'orange'):
        ower_red = np.array([20, 100, 100])
        upper_red = np.array([30, 255, 255])
    elif (a == 'blue'):
        lower_red = np.array([20, 100, 100])
        upper_red = np.array([30, 255, 255])
    # else:
    #     print("Wrong colour")


    # Driver program
    # if __name__ == "__main__":

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # start
    cv2.boundingRect(mask)
    # we are just adding 2 more channels on the mask so we can stack it along other images
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # ewhenuneunfenfen
    # e
    # e
    # e
    # e
    output = frame.copy()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    mask = cv2.medianBlur(mask, 5)
    x = int(frame.shape[1] / 2)
    y = int(frame.shape[0] / 2)
    cv2.line(frame, (x, y + 10), (x, y - 10), (255, 255, 255), 2)
    cv2.line(frame, (x + 10, y), (x - 10, y), (255, 255, 255), 2)
    # Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
    mask = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 3.5)

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

    # ensure at least some circles were found
    if circles is not None:
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
    success, bbox = tracker.update(res)
    print(bbox)
    if success:
        T_x  = drawBox(res, bbox,frame)
        print(T_x)
    else:
        cv2.putText(res, "Lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    cv2.putText(res, str(fps), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    stacked = np.hstack((res, frame))
    cv2.imshow('GUI OP !!!', cv2.resize(stacked, None, fx=0.8, fy=0.8))
    # cv2.imshow("Tracking", res)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break