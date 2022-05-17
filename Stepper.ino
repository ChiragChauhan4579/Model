#define speed 500
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(Serial.read());
  if(Serial.read()==97){
        Serial.println("Recived");
        digitalWrite(7,HIGH);
        for (int i=0;i<50;i++){
        delayMicroseconds(speed);
        digitalWrite(6,HIGH);
        delayMicroseconds(speed);  
        digitalWrite(6,LOW);
        }
        delay(2000);
        digitalWrite(7,LOW);
        for (int i=0;i<50;i++){
        delayMicroseconds(speed);
        digitalWrite(6,HIGH);
        delayMicroseconds(speed);  
        digitalWrite(6,LOW);
        }
  }
  
}
