#include <AFMotor.h>      
#include <Servo.h>              
#include <NewPing.h>      

#define TRIG_PIN 9 
#define ECHO_PIN 8 
#define MAX_DISTANCE 300 
#define MAX_SPEED 100
#define MAX_SPEED_OFFSET 40 
#define COLL_DIST 35 
#define TURN_DIST COLL_DIST+15 
NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE); 
 
AF_DCMotor leftMotor(2, MOTOR12_8KHZ); 
AF_DCMotor rightMotor(1, MOTOR12_8KHZ); 
Servo myservo;  

int leftDistance, rightDistance; 
int curDist = 0;
String motorSet = "";
int speedSet = 0;


void setup() {
  myservo.attach(10);   
  myservo.write(90); 
  delay(1000); 
 }

void loop() {
  myservo.write(90);  
  delay(90);
  curDist = readPing();  
  if (curDist < COLL_DIST) {changePath();}  
  moveForward();
  delay(500);
 }


void changePath() {
  moveStop();   
  myservo.write(10);  
    delay(500);
    leftDistance = readPing(); 
    delay(500);
    myservo.write(180);  
    delay(700);
    rightDistance = readPing(); 
    delay(500);
    myservo.write(90); 
    delay(100);
    compareDistance();
  }

  
void compareDistance()   
{
  if (leftDistance>rightDistance) 
  {
    turnLeft();
  }
  else if (rightDistance>leftDistance) 
  {
    turnRight();
  }
   else 
  {
    turnAround();
  }
}

int readPing() { 
  delay(70);   
  unsigned int uS = sonar.ping();
  int cm = uS/US_ROUNDTRIP_CM;
  return cm;
}

void moveStop() {leftMotor.run(RELEASE); rightMotor.run(RELEASE);}  

void moveForward() {
    motorSet = "FORWARD";
    leftMotor.run(FORWARD);      
    rightMotor.run(FORWARD); 
    for (speedSet = 0; speedSet < MAX_SPEED; speedSet +=2)    
    
  {
    leftMotor.setSpeed(100);
    rightMotor.setSpeed(100); 
    delay(5);
  }
}

void turnRight() {
  motorSet = "RIGHT";
  leftMotor.run(FORWARD);  
  rightMotor.run(BACKWARD);   
  rightMotor.setSpeed(speedSet+MAX_SPEED_OFFSET);      
  delay(350);      
  motorSet = "FORWARD";
  leftMotor.run(FORWARD);      
  rightMotor.run(FORWARD);
        
}  

void turnLeft() {
  motorSet = "LEFT" ;
  leftMotor.run(BACKWARD);      
  leftMotor.setSpeed(speedSet+MAX_SPEED_OFFSET);    
  rightMotor.run(FORWARD);     
  delay(350);  
  motorSet = "FORWARD";
  leftMotor.run(FORWARD);      
  rightMotor.run(FORWARD);     
 
}  

void turnAround() {
  motorSet = "TURNAROUND";
  leftMotor.run(FORWARD);      
  rightMotor.run(BACKWARD);    
  rightMotor.setSpeed(speedSet+MAX_SPEED_OFFSET);      
  
  delay(700); 
  motorSet = "FORWARD";
  leftMotor.run(FORWARD);      
  rightMotor.run(FORWARD);
       
}  


