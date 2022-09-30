import cv2
#  try......

KNOWN_DISTANCE = 76.2
KNOWN_WIDTH = 14

GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
fonts = cv2.FONT_HERSHEY_COMPLEX
cap = cv2.VideoCapture(0)        # if we have    stereo then second will go to 1

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def focal_length(measured_distance, real_width, width_in_rf_image):
    '''
This Function Calculate the Focal Length(distance between lens to sensor), it is a constant we can find by using
MEASURED_DISTANCE, REAL_WIDTH(Actual width of object) and WIDTH_OF_OBJECT_IN_IMAGE
:param1 Measure_Distance(int): It is distance measured from object to the Camera while Capturing Reference image

:param2 Real_Width(int): It is Act  ual width of object, in real world (like My face width is = 14.3 centimeters)
:param3 Width_In_Image(int): It is object width in the frame /image in our case in the reference image(found by Face detector) 
:return focal_length(Float):
'''
    focal_length_value = (width_in_rf_image * measured_distance) / real_width
    return focal_length_value

# distance estimation function
def distance_finder(focal_length, real_face_width, face_width_in_frame):
    '''
This Function simply Estimates the distance between object and camera using arguments(focal_length, Actual_object_width, Object_width_in_the_image)
:param1 focal_length(float): return by the focal_length_Finder function

:param2 Real_Width(int): It is Actual width of object, in real world (like My face width is = 5.7 Inches)
:param3 object_Width_Frame(int): width of object in the image(frame in our case, using Video feed)
:return Distance(float) : distance Estimated  

'''
    distance = (real_face_width * focal_length)/face_width_in_frame
    return distance

# face detector function 
def face_data(image):
    '''
    This function detects the face
    :param Takes image as argument.
    :returns face_width in the pixels
    '''

    face_width = 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), WHITE, 1)
        face_width = w

    return face_width


# reading reference image from directory
ref_image2 = cv2.imread("Ref_image.png")

ref_image2_face_width = face_data(ref_image2)
focal_length_found = focal_length(
    KNOWN_DISTANCE, KNOWN_WIDTH, ref_image2_face_width)
print(focal_length_found)
cv2.imshow("ref_image2", ref_image2)

while True:
    _, frame = cap.read()

    # calling face_data function
    face_width_in_frame = face_data(frame)
    # finding the distance by calling function Distance
    if face_width_in_frame != 0:
        Distance = distance_finder(
            focal_length_found, KNOWN_WIDTH, face_width_in_frame)
    # Drawing Text on the screen
        cv2.putText(
            frame, f"Distance = {round(Distance,2)} CM", (50, 50), fonts, 1, (WHITE), 2)
    cv2.imshow("frame", frame)
    cv2.imshow("original",ref_image2)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
