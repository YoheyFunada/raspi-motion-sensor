#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Tutorial Url:http://osoyoo.com/2017/03/15/raspberry-pi%E3%81%A7%E4%BA%BA%E4%BD%93%E6%84%9F%E7%9F%A5%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%82%92%E4%BD%9C%E5%8B%95%E3%81%97%E3%80%81led%E3%82%92/
#

import RPi.GPIO as GPIO             #importing the RPi.GPIO module
import time                        #importing the time module
GPIO.cleanup()                     #to clean up at the end of your script
motion_pin = 35                    #select the pin for the motion sensor
def init():
  GPIO.setmode(GPIO.BOARD)         #to specify which pin numbering system
  GPIO.setwarnings(False)
  GPIO.setup(motion_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #declare the motion_pin as an input
  print("-----------------------------------------------------------------------")

def main():
  while True:
    value=GPIO.input(motion_pin)
    if value!=0:                             #to read the value of a GPIO pin
      time.sleep(1)        #delay 2ms
      print "on"                           #print information
    else:
      time.sleep(1)       #delay 2ms
      print "off"                         #print information

init()
main()
GPIO.cleanup()
