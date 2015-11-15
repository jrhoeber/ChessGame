
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_StepperMotor *xMotor = AFMS.getStepper(200, 1);
Adafruit_StepperMotor *yMotor = AFMS.getStepper(200, 2);

int displacement = 130;
int displacementL = 160;
int displacementDiag = 184;
int displacementDiagL = 226;
int currX = 0;
int currY = 0;
int magPin = 7;
bool magOn = false;

bool moveBy(int x, int y);

void setup() {
  Serial.begin(57600);
  pinMode(magPin, OUTPUT);
  AFMS.begin();
  
  xMotor->setSpeed(40);
  yMotor->setSpeed(40);
  int xdir = 0;
}

void loop() {
/*  xMotor->step(100, FORWARD, DOUBLE);
  xMotor->step(100, BACKWARD, DOUBLE); 
  yMotor->step(100, FORWARD, DOUBLE);
  yMotor->step(100, BACKWARD, DOUBLE);*/

  if (Serial.available() > 3) {
    byte oposx = Serial.read();
    byte oposy = Serial.read();
    byte nposx = Serial.read();
    byte nposy = Serial.read();

    //Serial.write(oposx);
    //Serial.write(oposy);
    //Serial.write(nposx);
    //Serial.write(nposy);
    if(!moveBy(oposx - currX, oposy - currY))
    {
      return;
    }
    digitalWrite(magPin, HIGH);
    magOn = true;
    moveBy(nposx - oposx, nposy - oposy);
    digitalWrite(magPin, LOW);
    magOn = false;
    currX = nposx;
    currY = nposy;
  }  
}

bool moveBy(int x, int y)
{
  Serial.println("MoveBy");
  int xDir = (x < 0) + 1;
  int yDir = (y < 0) + 1;
  if(abs(x) == abs(y))
  {
    if(magOn){  
      for(int i = 0; i < displacementDiagL; i++)
      {
        xMotor->step(1, xDir, DOUBLE); 
        yMotor->step(1, yDir, DOUBLE);
      }
      for(int i = 0; i < (x-1)*displacementDiag; i++)
      {
        xMotor->step(1, xDir, DOUBLE); 
        yMotor->step(1, yDir, DOUBLE);
      }
    }else
    {
      for(int i = 0; i < (x)*displacementDiag; i++)
      {
       xMotor->step(1, xDir, DOUBLE); 
       yMotor->step(1, yDir, DOUBLE);
      }
    }
  } else if(x > 0 && y == 0)
  {
    if(magOn)
    {
      xMotor->step((x-1)*displacement+displacementL, xDir, DOUBLE);
    }
    else
    {
      xMotor->step(x*displacement, xDir, DOUBLE);
    }
  } else if(y > 0 && x == 0)
  {
    if(magOn)
    {
      yMotor->step((y-1)*displacement+displacementL, xDir, DOUBLE);
    }
    else
    {
      yMotor->step(y*displacement, yDir, DOUBLE);
    }
  } else{
    return false;
  }
  return true;
}

