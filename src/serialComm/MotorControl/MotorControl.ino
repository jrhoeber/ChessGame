
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_StepperMotor *xMotor = AFMS.getStepper(200, 1);
Adafruit_StepperMotor *yMotor = AFMS.getStepper(200, 2);

int displacement = 1234;
int displacementDiag = 1234;
int currX = 0;
int currY = 0;
int magPin = 7;

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
  byte oposx;
  byte oposy;
  byte nposx;
  byte nposy;
  if (Serial.available() > 3) {
    oposx = Serial.read();
    oposy = Serial.read();
    nposx = Serial.read();
    nposy = Serial.read();

    Serial.write(oposx);
    Serial.write(oposy);
    Serial.write(nposx);
    Serial.write(nposy);
  }
  if(!moveBy(oposx - currX, oposy - currY))
  {
    return;
  }
  digitalWrite(magPin, HIGH);
  moveBy(nposx - oposx, nposy - oposy);
  digitalWrite(magPin, LOW);
  currX = nposx;
  currY = nposy;
  
}

bool moveBy(int x, int y)
{
  int xDir = (x < 0) + 1;
  int yDir = (y < 0) + 1;
  if(abs(x) == abs(y))
  {
    for(int i = 0; i < x*displacement; i++)
    {
      xMotor->step(1, xDir, DOUBLE); 
      yMotor->step(1, yDir, DOUBLE);
    }
  } else if(x > 0 && y == 0)
  {
    xMotor->step(x*displacementDiag, xDir, DOUBLE);
  } else if(y > 0 && x == 0)
  {
    yMotor->step(y*displacement, yDir, DOUBLE);
  } else{
    return false;
  }
  return true;
}

