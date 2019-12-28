import RPi.GPIO as GPIO
import time
import sys

class Motor(object):
    '''Motor control'''
    def __init__(self,ENA,IN1,IN2,IN3,IN4,IN5,IN6,IN7,IN8,ENB):
        '''Specify motor pins'''
        #self.enab_pin=[ENA,ENB] #Enable pins
        self.inx_pin=[IN1,IN2,IN3,IN4,IN5,IN6,IN7,IN8] #Control pins
        
        self.RightAhead_pin=self.inx_pin[4]
        self.RightBack_pin=self.inx_pin[6]
        self.LeftAhead_pin=self.inx_pin[0]
        self.LeftBack_pin=self.inx_pin[2]

        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in self.inx_pin:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,GPIO.LOW)
        ppp=[0,0,0,0,0,0,0,0]
        for pin in range(8):
            GPIO.output(self.inx_pin[pin],ppp[pin])
        #pin=None

        #for pin in self.enab_pin:
            #GPIO.setup(pin,GPIO.OUT)
            #GPIO.output(pin,GPIO.HIGH)

    def ahead(self):
        #GPIO.output(self.RightAhead_pin,GPIO.HIGH)
        #GPIO.output(self.LeftAhead_pin,GPIO.HIGH)
        #GPIO.output(self.RightAhead_pin,GPIO.HIGH)
        #GPIO.output(self.LeftAhead_pin,GPIO.HIGH)
        ppp=[0,1,0,1,0,1,0,1]
        for pin in range(8):
            GPIO.output(self.inx_pin[pin],ppp[pin])
    def left(self):
        #for pin in self.inx_pin:
         #   GPIO.output(pin,GPIO.LOW)
        #GPIO.output(self.RightAhead_pin,GPIO.HIGH)
        #GPIO.output(self.LeftBack_pin,GPIO.HIGH)
        ppp=[0,1,0,1,1,0,1,0]
        for pin in range(8):
            GPIO.output(self.inx_pin[pin],ppp[pin])
    def right(self):
    #    for pin in self.inx_pin:
     #       GPIO.output(pin,GPIO.LOW)
      #  GPIO.output(self.LeftAhead_pin,GPIO.HIGH)
       # GPIO.output(self.RightBack_pin,GPIO.HIGH)
        ppp=[1,0,1,0,0,1,0,1]
        for pin in range(8):
            GPIO.output(self.inx_pin[pin],ppp[pin]) 
    def rear(self):
   #     for pin in self.inx_pin:
    #        GPIO.output(pin,GPIO.LOW)
     #   GPIO.output(self.RightBack_pin,GPIO.HIGH)
      #  GPIO.output(self.LeftBack_pin,GPIO.HIGH)
        ppp=[1,0,1,0,1,0,1,0]
        for pin in range(8):
            GPIO.output(self.inx_pin[pin],ppp[pin])
    def stop(self):
      #  for pin in self.inx_pin:
       #     GPIO.output(pin,GPIO.LOW)
        ppp=[0,0,0,0,0,0,0,0]
        for pin in range(8):
            GPIO.output(self.inx_pin[pin],ppp[pin])
    def clear(self):
        GPIO.cleanup()
