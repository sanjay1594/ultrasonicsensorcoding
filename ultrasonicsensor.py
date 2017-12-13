import RPi.GPIO as GPIO
import time
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    TRIG=23
    ECHO=24


    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)

    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end-pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    if distance >2 and distance <10:
        time.sleep(10)
        print "The Bin is Full-Needed to change Immediately"
        
    GPIO.cleanup()
