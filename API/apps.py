from django.apps import AppConfig
import RPi.GPIO as GPIO
import time

class ApiConfig(AppConfig):
    name = 'API'
    def ready(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(27,GPIO.OUT)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        
          
          