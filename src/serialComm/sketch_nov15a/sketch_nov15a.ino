
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);
int mmDisplacement = 1234;

void setup() {
  Serial.begin(57600);           // set up Serial library at 9600 bps

  AFMS.begin();
  //AFMS.begin(1000);
  
  myMotor->setSpeed(40); 
  int xdir = 0;
}

void loop() {
  //myMotor->step(50, FORWARD, DOUBLE); 
  //myMotor->step(50, BACKWARD, DOUBLE);  
  int oposx;
  int oposy;
  int nposx;
  int nposy;
  if (Serial.available() > 3) {
    oposx = Serial.read();
    oposy = Serial.read();
    nposx = Serial.read();
    nposy = Serial.read();
    
    // say what you got:
    Serial.print("I received: ");
    Serial.println(oposx, DEC);
    Serial.println(oposy, DEC);
    Serial.println(nposx, DEC);
    Serial.println(nposy, DEC);
  }
}

