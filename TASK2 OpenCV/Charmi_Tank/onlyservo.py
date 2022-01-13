import RPi.GPIO as gpio
import time



#set
gpio.setmode(gpio.BOARD)
gpio.setup(35,gpio.OUT)
gpio.setup(33, gpio.OUT)
pwm=gpio.PWM(35, 50)
pwm2 = gpio.PWM(33,50)
pwm.start(0)
pwm2.start(1)
print('waiting for 2 seconds')
time.sleep(2)

print('Rotating 180 degree in 10 degree')


duty=2

while duty<=12:
    pwm2.ChangeDutyCycle(duty)
    pwm.ChangeDutyCycle(duty)
    
    time.sleep(1)
    duty=duty+1

time.sleep(2)

print('Turning back to 90 degree for 2 sec')

pwm.ChangeDutyCycle(7)
pwm2.ChangeDutyCycle(7)
time.sleep(2)

print('0')
pwm.ChangeDutyCycle(2)
pwm2.ChangeDutyCycle(2)
time.sleep(0.5)
pwm.ChangeDutyCycle(0)
pwm2.ChangeDutyCycle(0)
pwm.stop()
pwm2.stop()
gpio.cleanup()
print('Goodbye')


