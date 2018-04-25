
import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setwarnings(False)
SIM808_PWR_CTRL = 18 #BCM PIN 17(BOARD PIN 11)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SIM808_PWR_CTRL,GPIO.OUT)
GPIO.output(SIM808_PWR_CTRL,GPIO.HIGH)
time.sleep(3)
GPIO.output(SIM808_PWR_CTRL,GPIO.LOW)
time.sleep(1)