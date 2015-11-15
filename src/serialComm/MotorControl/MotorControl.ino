
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_StepperMotor *xMotor = AFMS.getStepper(200, 1);
Adafruit_StepperMotor *yMotor = AFMS.getStepper(200, 2);

int displacement = 130;
int displacementL = 130;
int displacementDiag = 180;
int displacementDiagL = 180;
int currX = 0;
int currY = 0;
int magPin = 7;
bool magOn = false;

bool moveBy(int x, int y);

void setup() {
  Serial.begin(9600);
  pinMode(magPin, OUTPUT);
  AFMS.begin();
  
  xMotor->setSpeed(40);
  yMotor->setSpeed(40);
  /*for(int i = 0; i < 6*displacementDiag; i++)
      {
        xMotor->step(1, BACKWARD, DOUBLE); 
        yMotor->step(1, BACKWARD, DOUBLE);
      }*/
  
  //xMotor->step(displacement*1, BACKWARD, DOUBLE);
  //yMotor->step(displacement*6, BACKWARD, DOUBLE);
}

void loop() {
  if (Serial.available() > 3) {
    byte oposx = Serial.read() - 48;
    byte oposy = Serial.read() - 48;
    byte nposx = Serial.read() - 48;
    byte nposy = Serial.read() - 48;

    Serial.print(oposx);
    Serial.print(oposy);
    Serial.print(nposx);
    Serial.print(nposy);
    moveBy(oposx - currX, oposy - currY);
    digitalWrite(magPin, HIGH);
    magOn = true;
    delay(500);
    moveBy(nposx - oposx, nposy - oposy);
    digitalWrite(magPin, LOW);
    magOn = false;
    delay(500);
    currX = nposx;
    currY = nposy;
    Serial.println("DONE");
  }  
}

bool moveBy(int x, int y)
{
  if(x == 0 && y == 0){
    return false;
  }
  int xDir = (x < 0) + 1;
  int yDir = (y < 0) + 1;
  Serial.println(xDir);
  Serial.println(yDir);
  x = abs(x); y = abs(y);
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
      yMotor->step((y-1)*displacement+displacementL, yDir, DOUBLE);
    }
    else
    {
      yMotor->step(y*displacement, yDir, DOUBLE);
    }
  } else if(!magOn)
  {
    x = x*displacement;
    y = y*displacement;
    if(x < y)
    {
      for(int i = 0; i < x; i++){
        xMotor->step(1, xDir, DOUBLE);
        yMotor->step(1, yDir, DOUBLE);
        x--;
        y--;
      }
      for(int i = 0; i < y; i++){
        yMotor->step(1, yDir, DOUBLE);
      }
    }
    else if(x > y)
    {
      for(int i = 0; i < y; i++){
        xMotor->step(1, xDir, DOUBLE);
        yMotor->step(1, yDir, DOUBLE);
        x--;
        y--;
      }
      for(int i = 0; i < x; i++){
        yMotor->step(1, yDir, DOUBLE);
      }
    }
  } else
  {
    return false;
  }
  return true;
}

