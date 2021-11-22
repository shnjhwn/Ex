# Test System

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Proximity_PIN = 22 # wPi: 3 / BCM: 22
GPIO.setup(Proximity_PIN, GPIO.IN)

LED_PIN = 19 # wPi: 24 / BCM: 19 | PWM 1
GPIO.setup(LED_PIN, GPIO.OUT)

P_LED = GPIO.PWM(LED_PIN, 100)
P_LED.start(0)

RGB_PIN = 12 # wPi: 26 / BCM: 12 | PWM 0
GPIO.setup(RGB_PIN, GPIO.OUT)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

P_R = GPIO.PWM(4, 2000)
P_G = GPIO.PWM(2, 2000)
P_B = GPIO.PWM(3, 2000)
P_R.start(0)
P_G.start(0)
P_B.start(0)

DC_MOTOR = 13 # wPi: 23 / BCM: 13 | PWM 1
GPIO.setup(DC_MOTOR, GPIO.OUT)

P_DC = GPIO.PWM(DC_MOTOR, 100)
P_DC.start(0)

try:
    while True:
	GPIO.output(DC_MOTOR, True)
	P_DC.ChangeDutyCycle(100)
	if GPIO.input(Proximity_PIN) == False:
	    P_DC.ChangeDutyCycle(0)
	    print "Near Proximity Sensor!"
	    P_LED.ChangeDutyCycle(0)
	    for x in range(5):
		P_R.ChangeDutyCycle(100)
		time.sleep(0.1)
		P_R.ChangeDutyCycle(0)
		time.sleep(0.1)
	else :
	    P_R.ChangeDutyCycle(0)
	    P_LED.ChangeDutyCycle(100)
	    time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    P_LED.stop()
    P_R.stop()
    P_G.stop()
    P_B.stop()
    P_DC.stop()
