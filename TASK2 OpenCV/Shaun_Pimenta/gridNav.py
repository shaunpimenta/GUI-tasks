if x>int(frame.shape[1] / 2) and y>int(frame.shape[0] / 2) and x>int(frame.shape[1] / 2)+30 and y>int(frame.shape[0]/2)+30 and x<int(frame.shape[1] / 2)+100and y<int(frame.shape[0]/2)+100:
        cv2.putText(frame, "Circle is towards bottom right!!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        right_move(Xposition, Yposition)
elif x > int(frame.shape[1] / 2) and y > int(frame.shape[0] / 2) and x > int(frame.shape[1] / 2) + 100 and y > int(frame.shape[0] / 2) + 100:
        cv2.putText(frame, "Circle is towards extreme bottom right!!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),2)
elif x<int(frame.shape[1] / 2) and y>int(frame.shape[0] / 2) and x<int(frame.shape[1] / 2)+30 and y>int(frame.shape[0]/2)+30 and x<int(frame.shape[1] / 2)+35 and y>int(frame.shape[0]/2)+30:
        cv2.putText(frame, "Circle is towards bottom left !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        left_move(Xposition, Yposition)
elif x<int(frame.shape[1] / 2) and y>int(frame.shape[0] / 2) and x<int(frame.shape[1] / 2)+35 and y>int(frame.shape[0]/2)+35:
        cv2.putText(frame, "Circle is towards extreme bottom left !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
elif x<int(frame.shape[1] / 2) and y<int(frame.shape[0] / 2)and x<int(frame.shape[1] / 2)+30 and y<int(frame.shape[0]/2)+30:
        cv2.putText(frame, "Circle is towards top left !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        left_move(Xposition, Yposition)
elif x<int(frame.shape[1] / 2) and y<int(frame.shape[0] / 2)and x<int(frame.shape[1] / 2)+35 and y<int(frame.shape[0]/2)+35:
        cv2.putText(frame, "Circle is towards extreme top left !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
elif x>int(frame.shape[1] / 2) and y<int(frame.shape[0] / 2)and x>int(frame.shape[1] / 2)+30 and y<int(frame.shape[0]/2)+30:
        cv2.putText(frame, "Circle is towards top right !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        right_move(Xposition, Yposition)
elif x>int(frame.shape[1] / 2) and y<int(frame.shape[0] / 2)and x>int(frame.shape[1] / 2)+35 and y<int(frame.shape[0]/2)+35:
        cv2.putText(frame, "Circle is towards extreme top right !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
elif x!=0:
        cv2.putText(frame, "Circle is right in front !!", (75, 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        # landing
