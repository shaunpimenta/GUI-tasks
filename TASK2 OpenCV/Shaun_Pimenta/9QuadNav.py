        if x < int(frame.shape[1] / 2) - 30 and y < int(frame.shape[0] / 2) - 30:
            print('The circle is in top right ')
            pass #'top right'
        elif x>int(frame.shape[1]/2+30) and y < int(frame.shape[0]/2-30):
            print("The circle is in top left")
            pass #top left
        elif x > int(frame.shape[1] / 2 - 30) and y < int(frame.shape[0] / 2 + 30):
            print("The circle is in bottom left")
            pass #bottom left
        elif x > int(frame.shape[1] / 2 + 30) and y > int(frame.shape[0] / 2 + 30):
            print("The circleis in bottom right")
            pass #bottom right
        elif (w+30)<x<(w+30) and y<h-30:
            print("Circle is in center left") #top center box
        elif (w + 30) < x < (w + 30) and y > h+30:
            pass #bottom center box
        elif (h-30)<x<(h+30) and y<w-30:
            print("Circle is in right center box") #right center box (from plane perspective)
        elif (h - 30) < x < (h + 30) and y > w + 30:
            print("Circle is in center left")
            pass #left center box (from plane perspective)
        else :
            print("Circle is in center !!")
        print("STOP")
