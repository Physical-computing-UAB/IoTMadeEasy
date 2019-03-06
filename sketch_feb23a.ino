#define echopin  8 // echo pin
#define trigpin 9 // Trigger pin


int maximumRange = 30;
long duration, distance;

void setup() {
  Serial.begin (9600);
  pinMode (trigpin, OUTPUT);
  pinMode (echopin, INPUT );
  pinMode (4, OUTPUT);
  pinMode (5, OUTPUT);
  pinMode (13, OUTPUT);
  pinMode (6, OUTPUT);
  pinMode (7, OUTPUT);
}

void loop ()
{

  {
    digitalWrite(trigpin,LOW);
    delayMicroseconds(2);
    
    digitalWrite(trigpin,HIGH);
    delayMicroseconds(10);
    
    duration=pulseIn (echopin,HIGH);
    
    distance= duration/58.2;
    delay (50);
    Serial.println(distance);
  }
  
  if (distance >= 30 ){
    digitalWrite(4,HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(6,LOW);
    digitalWrite(7,LOW);
    delay (200);
  }
  
  else if (distance >=15 && distance <= 25) {
    digitalWrite (4,HIGH);
    digitalWrite (5,LOW);
    digitalWrite (6,LOW);
    digitalWrite (7,LOW);
    delay (1000);
  }
 else if (distance < 15){
   digitalWrite (4, LOW);
   digitalWrite (5, LOW);
   digitalWrite (6,HIGH);
   digitalWrite (7,HIGH);
   delay (1000);
   digitalWrite (4,LOW);
   digitalWrite (5,HIGH);
   digitalWrite (6,LOW);
   digitalWrite (7, LOW);
   delay (1000);
   
     
 }

}
