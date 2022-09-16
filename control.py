
import RPi.GPIO as GPIO
import time


def init():
    global in1, in2, en, p, servo
    in1 = 18
    in2 = 16
    en = 22

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    p = GPIO.PWM(en, 1000)
    p.start(25)
    GPIO.setup(7, GPIO.OUT)
    servo = GPIO.PWM(7, 50)
    servo.start(0)


def forward():
    servo.ChangeDutyCycle(7.15)
    p.ChangeDutyCycle(75)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)


def reverse():
    servo.ChangeDutyCycle(7.15)
    p.ChangeDutyCycle(75)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)


def forward_left():
    p.ChangeDutyCycle(50)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    servo.ChangeDutyCycle(4.65)


def backward_left():
    servo.ChangeDutyCycle(4.65)
    p.ChangeDutyCycle(75)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)


def backward_right():
    servo.ChangeDutyCycle(12.15)
    p.ChangeDutyCycle(75)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)


def forward_right():
    p.ChangeDutyCycle(50)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    servo.ChangeDutyCycle(12.15)


def neutral():
    p.ChangeDutyCycle(50)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    servo.ChangeDutyCycle(7.15)

# Set GPIO numbering mode
# Set pin 11 as an output, and define as servo1 as PWM pin


# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)
