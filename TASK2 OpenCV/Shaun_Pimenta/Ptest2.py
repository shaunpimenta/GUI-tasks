import cv2 as cv
import numpy as np
cv.__version__
vid=cv.VideoCapture(0)
while True:
    some, frame = vid.read()
    #     hs_fra=cv.cvtColor(fra,cv.COLOR_BGR2HSV)

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of red color in HSV
    #     if (a == 'red'):
    lower_red = np.array([160, 50, 50])
    upper_red = np.array([200, 255, 255])
    cv.line(frame, (int(frame.shape[1] / 2), 0), (int(frame.shape[1] / 2), int(frame.shape[0])), (255, 255, 255), 5)
    cv.line(frame, (0, int(frame.shape[0] / 2)), (int(frame.shape[1]), int(frame.shape[0] / 2)), (255, 255, 255), 5)
    #     elif (a == 'green'):
    #     lower_green = np.array([50, 100, 100])
    #     upper_green= np.array([70, 255, 255])
    # #     elif (a == 'yellow'):
    #     lower_yellow = np.array([20, 100, 100])
    #     upper_yellow = np.array([30, 255, 255])
    # #     elif (a == 'white'):
    #     lower_white = np.array([0, 0, 255])
    #     upper_white= np.array([255, 255, 255])
    # #     elif (a == 'orange'):
    #     lower_orange = np.array([20, 100, 100])
    #     upper_orange = np.array([30, 255, 255])
    # #     elif (a == 'blue'):
    #     lower_blue = np.array([20, 100, 100])
    #     upper_blue = np.array([30, 255, 255])
    # #     cv.imshow("frame",fra)

    red_mask = cv.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    redd = cv.bitwise_and(frame, frame, mask=red_mask)
    #     red_mask=cv.erode(red_mask,np.ones((5,5),np.uint8))
    #     contours, _ = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #     redd =cv.boundingRect(redd)
    op = frame.copy()

    gray = cv.cvtColor(redd, cv.COLOR_BGR2GRAY)

    gray = cv.GaussianBlur(gray, (5, 5), 0)
    gray = cv.medianBlur(gray, 5)
    #     gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                                  cv.THRESH_BINARY, 11, 3.5)

    #     kernel = np.ones((2, 3), np.uint8)
    #     gray = cv.erode(gray, kernel, iterations=1)
    # gray = erosion

    #     gray = cv.dilate(gray, kernel, iterations=1)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.2, 100)

    #     circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=1000)
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv.circle(op, (x, y), r, (0, 255, 0), 4)
            cv.rectangle(op, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            # cv.line(op, (x, y), (300, 400), (0, 255, 0), thickness=2)
            cv.line(op, (x, y), (int(frame.shape[1]/2), int(frame.shape[0]/2)), (0, 255, 0), thickness=5)
            dis= ((x-int(frame.shape[1]/2))**2-(y-int(frame.shape[0]/2)))**0.5
            print(f'Distance is {dis}')
            # print(int(frame.shape[0]))
            # cv.circle(output, (x, y), r, (0, 255, 0), 4)
            # cv.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            r = str(r)
            rc= int(r)

            diameter = 2 * r
            rcm = (2.54/96)*rc
            a = f'Radius is {rcm}'
            b = f'Center is ({x},{y})'
            cv.putText(op, b, (x - 5 + 80, y - 5 + 120), cv.FONT_HERSHEY_COMPLEX, 0.7,
                       (255, 255, 255), 1)
            cv.putText(op, a, (x - 5 + 10, y - 5 + 60), cv.FONT_HERSHEY_COMPLEX, 0.7,
                       (100, 255, 255), 4)
            # time.sleep(0.5)
            # print("Column Number: ")
            # print(x)
            # print("Row Number: ")
            # print(y)
            print("Radius is: ")
            print(rcm)
            print(f"Center is ({x},{y})")
        # show the output image
    #         cv.imshow("output", np.hstack([frame, op]))
    #         cv.waitKey(0)#     for i in contours:
    #         are=cv.contourArea(i)
    #         approx=cv.approxPolyDP(i,20*cv.arcLength(i,True),True)
    #         print(are)
    #         if are>500:
    #             cv.drawContours(frame, [approx], 0, (0, 0, 0),5)
    #             print(len(approx))
    #     cv.drawContours()
    #         area = cv.contourArea(i)
    #         approx = cv.approxPolyDP(i, 0.02*cv.arcLength(cnt, True), True)
    #         x = approx.ravel()[0]
    #         y = approx.ravel()[1]

    #     green_mask = cv.inRange(hsv, lower_green, upper_green)
    #     # Bitwise-AND mask and original image
    #     greenn = cv.bitwise_and(frame, frame, mask=green_mask)

    #     yellow_mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    #     # Bitwise-AND mask and original image
    #     yelloww = cv.bitwise_and(frame, frame, mask=yellow_mask)

    #     blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
    #     # Bitwise-AND mask and original image
    #     bluee = cv.bitwise_and(frame, frame, mask=blue_mask)

    #     white_mask = cv.inRange(hsv, lower_white, upper_white)
    #     # Bitwise-AND mask and original image
    #     whitee = cv.bitwise_and(frame, frame, mask=white_mask)

    #     orange_mask = cv.inRange(hsv, lower_orange, upper_orange)
    #     # Bitwise-AND mask and original image
    #     orrangee = cv.bitwise_and(frame, frame, mask=orange_mask)
    #     detect_cir(frame)

    cv.imshow("frame", frame)
    cv.imshow("op", op)
    #     cv.imshow("green",greenn)

    cv.imshow("red", redd)

    #     red_masks = cv.inRange(hsv, lower_red, upper_red)
    #     # Bitwise-AND mask and original image
    #     redd = cv.bitwise_and(frame, frame, mask=red_mask)
    #     red_masks=cv.erode(red_mask,np.ones((5,5),np.uint8))
    #     contours, _ = cv.findContours(red_masks, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #     for i in contours:
    # #         approx=cv.approxPolyDP(i,0.01*cv.arcLength(i,True),True)
    #         cv.drawContours(frame, [i], 0, (0, 0, 0),5)
    #         cv.imshow("count",frame)
    #     cv.drawContours(frame, [approx], 0, (0, 0, 0), 5)
    #     cv.imshow("blue",bluee)
    #     cv.imshow("orange",orangee)
    #     cv.imshow("white",whitee)
    #     cv.imshow("yellow",yelloww)

    if cv.waitKey(20) & 0xFF == ord('q'):
        vid.release()
        break
vid.release()
cv.destroyAllWindows()
cv.waitKey(1)


# def detect_cir(fram):
#     circles = cv.HoughCircles(fram, cv.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=1000)
#     # print circles
#
#     # ensure at least some circles were found
#     if circles is not None:
#         # convert the (x, y) coordinates and radius of the circles to integers
#         circles = np.round(circles[0, :]).astype("int")
#
#         # loop over the (x, y) coordinates and radius of the circles
#         for (x, y, r) in circles:
#             # draw the circle in the output image, then draw a rectangle in the image
#             # corresponding to the center of the circle
#             cv.circle(output, (x, y), r, (0, 255, 0), 4)
#             cv.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
#             r = str(r)
#             diameter = 2 * r
#             a = f'Radius is {r}'
#             b = f'Center is ({x},{y})'
#             cv.putText(output, b, (x - 5 + 80, y - 5 + 120), cv.FONT_HERSHEY_COMPLEX, 0.7,
#                         (255, 255, 255), 4)
#             cv.putText(output, a, (x - 5 + 10, y - 5 + 60), cv.FONT_HERSHEY_COMPLEX, 0.7,
#                         (100, 255, 255), 4)
#             # time.sleep(0.5)
#             print("Column Number: ")
#             print(x)
#             print("Row Number: ")
#             print(y)
#             print("Radius is: ")
#             print(r)
#             print(f"Center is ({x},{y})")
