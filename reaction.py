# Author: Nie Yujin
# Date: 10/4/25
# A reaction game with LED
# version 1: turn on and off the LED for 5 second

from gpiozero import LED,Button
from time import sleep

# name the pin
led=LED(4)
# turn on the LED
led.on()
# light on the LED for 5 second
sleep(5)
# turn off the LED
led.off()

