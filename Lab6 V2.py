from picamera import PiCamera
from gpiozero import Button
from datetime import datetime
from time import sleep
import os


camera = PiCamera()
sleep(2)
camera.capture("/home/pi/Documents/Programs/Lab6/hello.jpg")

sleep(5) #this sleep simulates the evaluation of the image, between the os.remove and the capture
         #will contain photo recignition

os.remove("hello.jpg")