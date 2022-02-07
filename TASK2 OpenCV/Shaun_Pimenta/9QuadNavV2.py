import cv2
cap = cv2.VideoCapture(0)
x=int(input("Enter x : "))
y=int(input("Enter y : "))
c=80 #width of the center box
while True:
        _,frame= cap.read()
        h = int(frame.shape[0] / 2)
        w = int(frame.shape[1] / 2)
        print(f"{w}\n{h}")
        # cv2.line(frame, (w, 0), (w, 2 * h), (0, 255, 0), 2)
        # cv2.line(frame, (0, h), (2 * w, h), (0, 255, 0), 2)
        cv2.rectangle(frame, (w-c, h-c), ( w+c, h+c), (0, 255, 0), 2)
        cv2.rectangle(frame, (0, 0), ( w-c, h-c), (0, 255, 0), 2)
        cv2.rectangle(frame, (w+c, 0), (2*w, h - c), (0, 255, 0), 2)
        cv2.rectangle(frame, (0, h+c), (w - c, 2*h), (0, 255, 0), 2)
        cv2.rectangle(frame, (w + c, h + c), (2*w, 2*h), (0, 255, 0), 2)
        # ///////////////////////////////////////////////////////////////
        if x < w - c and y < h - c:
                print('The circle is in top right ')
                pass  # 'top right'
        elif x > w + c and y < h - c:
                print("The circle is in top left")
                pass  # top left
        elif x<w-c and y>h+c:
                print("The circle is in bottom left")
                pass
        elif x > int(w + c) and y > int(h + c):
                print("The circle is in bottom right")
                pass  # bottom right
        elif (w - c) < x < (w + c) and y < h - c:
                print("Circle is in center top")  # top center box
                pass
        elif (w - c) < x < (w + c) and y > h + c:
                print("Circle is in bottom center")
                pass  # bottom center box
        elif (h - c) < y < (h + c) and x < w - c:
                print("Circle is in left center box")  # right center box (from plane perspective)
        elif (h - c) < y < (h + c) and x > w + c:
                print("Circle is in left center box")
                pass  # left center box (from plane perspective)
        else:
                print("Circle is in center !!")
        print("STOP")
        cv2.line(frame,(w,h),(x,y),(0, 255, 0), 2)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
                break
cv2.destroyAllWindows()
