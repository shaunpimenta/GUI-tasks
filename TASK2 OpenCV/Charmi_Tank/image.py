from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
impoet pandas as pd
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# grab an image from the camera
print("image is captured")

camera.capture(rawCapture, format="bgr")
image = rawCapture.array
time.sleep(0.5)
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)
