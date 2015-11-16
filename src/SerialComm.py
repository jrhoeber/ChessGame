import serial
from string import *
import time
class SerialComm:
    def __init__(self):
        #TODO: Scan for Arduino on USB
        self.arduinoSerial = serial.Serial("/dev/cu.usbmodemFD121", baudrate=9600)
        time.sleep(2)

    def moveToPosition(self, opos, npos):
        #TODO: Clean Up
        s = str(opos[0]),str(opos[1]),str(npos[0]),str(npos[1]) , "\n"
        self.arduinoSerial.write(s[0])
        self.arduinoSerial.write(s[1])
        self.arduinoSerial.write(s[2])
        self.arduinoSerial.write(s[3])
        self.arduinoSerial.read() 
    def closeConnection(self):
        self.arduinoSerial.close()
