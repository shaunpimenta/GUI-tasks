import RPi.GPIO as GPIO
import time

l = 0
r = 0

lServoPin = 35
rServoPin = 33
GPIO.setmode(GPIO.BOARD)

GPIO.setup(lServoPin, GPIO.OUT)
GPIO.setup(rServoPin, GPIO.OUT)

lPwm = GPIO.PWM(lServoPin, 50)
rPwm = GPIO.PWM(rServoPin, 50)
lPwm.start(5)
rPwm.start(5)

while(l < 5):
    for i in range(45, 135):
        position = 1./18.*(i)+2
        lPwm.ChangeDutyCycle(position)
        time.sleep(0.005)

    for i in range(135, 45, -1):
        position = 1./18.*(i)+2
        lPwm.ChangeDutyCycle(position)
        time.sleep(0.005)
    l = l + 1
lPwm.stop()

while(r < 5):
    for i in range(135, 45, -1):
        position = 1./18.*(i)+2
        rPwm.ChangeDutyCycle(position)
        time.sleep(0.005)

    for i in range(45, 135):
        position = 1./18.*(i)+2
        rPwm.ChangeDutyCycle(position)
        time.sleep(0.005)
    r = r + 1
rPwm.stop()
GPIO.cleanup()