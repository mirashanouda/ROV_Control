  #include <Wire.h>
#include "Servo.h"
//5,10,12,14,2,4,6,8
#define pinA 6
#define pinB 12
#define pinC 5
#define pinD 14
#define pinE 8
#define pinF 2

#define led_pin 13
#define grip_pin 33

Servo A, B, C, D, E, F;

int motorvalA = 1500, motorvalB = 1500, motorvalC = 1500, motorvalD = 1500, motorvalE = 1500, motorvalF = 1500;
int led = 0, gripper = 0;

void setup(void) 
{
  Serial.begin(57600);
    init_thrusters();
}


void loop(void) 
{
  motor_values();
  moveROV(); 
  //delay(1000);    
}


void init_thrusters()
{
   A.attach(pinA);
   B.attach(pinB);
   C.attach(pinC);
   D.attach(pinD);
   E.attach(pinE);
   F.attach(pinF);
   
   A.writeMicroseconds(1500);
   B.writeMicroseconds(1500);
   C.writeMicroseconds(1500);
   D.writeMicroseconds(1500);
   E.writeMicroseconds(1500);
   F.writeMicroseconds(1500);
    
   pinMode(grip_pin, OUTPUT);
   pinMode(led_pin, OUTPUT);
  //END OF THRUSTERS
}

void motor_values()  //  this void required to separate the string data into motor values
{
  motorvalA = 1500; 
  motorvalB = 1500;
  motorvalC = 1500;
  motorvalD = 1500;
  motorvalE = 1500;
  motorvalF = 1500;
  gripper   = 1;
  led       = 1;
  
}
  
void moveROV()
{
  if(motorvalA > 1900 || motorvalA < 1100)
      motorvalA = 1500;
  if(motorvalB > 1900 || motorvalB < 1100)
      motorvalB = 1500;
  if(motorvalC > 1900 || motorvalC < 1100)
      motorvalC = 1500;
  if(motorvalD > 1900 || motorvalD < 1100)
      motorvalD = 1500;
  if(motorvalE > 1900 || motorvalE < 1100)
      motorvalE = 1500;
  if(motorvalF > 1900 || motorvalF < 1100)
      motorvalF = 1500;
      
  A.writeMicroseconds (motorvalA);
  Serial.print(motorvalA); 
  B.writeMicroseconds (motorvalB);
  C.writeMicroseconds (motorvalC);
  D.writeMicroseconds (motorvalD);
  E.writeMicroseconds (motorvalE);
  F.writeMicroseconds (motorvalF);
  
  digitalWrite(led_pin, LOW);
  digitalWrite(grip_pin, LOW);
}
