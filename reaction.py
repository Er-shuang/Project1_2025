# Version 2
# Author: Xuanru Guo
# Add an element of surprise

# import modules and libraries
from gpiozero import LED, Button
from time import sleep
from random import uniform

# set up the pin
led = LED(4)

# wait for 5 seconds and turn the LED on
led.on()
# the length of time is random
sleep(uniform(5,10))
led.off()


