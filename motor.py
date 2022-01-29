#  Reference:
# https://www.aranacorp.com/en/control-a-stepper-with-raspberrypi

import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# Instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use Pins 18,22,24,26 GPIO24,GPIO25,GPIO8,GPIO7
StepPins = [24,25,8,7]
# Set all pins as output
for pin in StepPins:
        print("Setup pins")
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)
# Define some settings
WaitTime = 0.005

# Define simple sequence
StepCount = 4
Seq = []
Seq = [i for i in range(0, StepCount)]
Seq[0] = [1,0,0,0]
Seq[1] = [0,1,0,0]
Seq[2] = [0,0,1,0]
Seq[3] = [0,0,0,1]


def steps(nb):
        StepCounter = 0
        if nb<0: sign=-1
        else: sign=1
        nb=sign*nb*2 #times 2 because half-step
        print("nbsteps {} and sign {}".format(nb,sign))
        for i in range(nb):
                for pin in range(4):
                        xpin = StepPins[pin]
                        if Seq[StepCounter][pin]!=0:
                                GPIO.output(xpin, True)
                        else:
                                GPIO.output(xpin, False)
                StepCounter += sign
        # If we reach the end of the sequence
        # start again
                if (StepCounter==StepCount):
                        StepCounter = 0
                if (StepCounter<0):
                        StepCounter = StepCount-1
                # Wait before moving on
                time.sleep(WaitTime)

# Start main loop
nbStepsPerRev=1024
if __name__ == '__main__' :
    hasRun=False
    while not hasRun:
            steps(nbStepsPerRev)
            time.sleep(1)
            steps(-nbStepsPerRev)
            time.sleep(1)

            hasRun=True

    print("Stop motor")
    for pin in StepPins:
            GPIO.output(pin, False)
