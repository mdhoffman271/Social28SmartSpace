# Reference: https://projects.raspberrypi.org/en/projects/physical-computing/12

from gpiozero import DistanceSensor

ultrasonic = DistanceSensor(echo=17, trigger=4)

while True:
    print(ultrasonic.distance)