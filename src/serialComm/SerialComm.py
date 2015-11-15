import serial
from string import *
import time
class SerialComm:
    def __init__(self):
        self.arduinoSerial = serial.Serial("/dev/cu.usbmodemFD121", baudrate=9600)
        time.sleep(2)

    def moveToPosition(self, opos, npos):
        s = str(opos[0]),str(opos[1]),str(npos[0]),str(npos[1]) , "\n"
        self.arduinoSerial.write(s[0])
        self.arduinoSerial.write(s[1])
        self.arduinoSerial.write(s[2])
        self.arduinoSerial.write(s[3])
    
    def closeConnection(self):
        self.arduinoSerial.close()

s = SerialComm()
s.moveToPosition([1,1], [3,3])


