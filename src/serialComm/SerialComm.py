import serial
import numpy as np
from printrun.printcore import printcore
from printrun import gcoder

class SerialComm:
    def __init__(self):
        self.arduinoSerial = serial.Serial("/dev/cu.usbmodemFD121", baudrate=57600)

    def moveToPosition(self, opos, npos):
        s = str(opos[0])+str(opos[1])+str(npos[0])+str(npos[1])
        print s
        self.arduinoSerial.write(s)
        #print self.arduinoSerial.read()

s = SerialComm()
s.moveToPosition([1,2], [3,4])


