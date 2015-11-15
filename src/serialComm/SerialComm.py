import serial
import numpy as np
from printrun.printcore import printcore
from printrun import gcoder

class SerialComm:
    def __init__(self):
        self.offset = 10.
        xaxis = np.arange(8)
        yaxis = np.arange(8)
        self.xgrid, self.ygrid = np.meshgrid(xaxis, yaxis)
        print self.xgrid*self.offset, '\n', self.ygrid*self.offset
        self.printer = printcore()#"/dev/cu.usbserial-AH016TB8", 19200)
        if self.printer.connect("/dev/cu.usbserial-AH016TB8", 19200):
            print "ERROR"
        gcode=[i.strip() for i in open('tester.gcode.txt')] # or pass in your own array of gcode lines instead of reading from a file
        gcode = gcoder.LightGCode(gcode)
        self.printer.startprint(gcode)

    def printGCodeFromFile(self, fileName):
        gcode=[i.strip() for i in open(fileName)]
        gcode = gcoder.LightGCode(gcode)
        p.startprint(gcode)

    def printGCodeFromArray(self, gcode):
        gcode = gcoder.LightGCode(gcode)
        p.startprint(gcode)

    def generateGCodeForPos(position):
        gcode = "X"+itoa(position[0]), "Y"+itoa(position[1])
        print gcode
    
    def moveToPosition(self, xpos, ypos):
        position = self.xgrid[xpos[0]], self.ygrid[ypos[0]]
        newPosition = self.xgrid[xpos[1]], self.ygrid[ypos[1]]
        generateGCodeForPos(position)


s = SerialComm()
#s.moveToPosition(1,2)

