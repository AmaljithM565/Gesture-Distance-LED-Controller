#include <Arduino.h>
int ledPins[4]={13,12,14,27};

void setup(){
  Serial.begin(115200);
  for(int i=0;i<4;i++){
    pinMode(ledPins[i],OUTPUT);
    digitalWrite(ledPins[i],LOW);
  }
  Serial.println("ESP32 ready");
}

void loop(){
  if(Serial.available()){
    int level=Serial.parseInt();
    if(level>=0 && level<=4){
      Serial.print("Level received:");
      Serial.print(level);

      for(int i=0;i<4;i++){
        if(i<level)
          digitalWrite(ledPins[i],HIGH);
        else
          digitalWrite(ledPins[i],LOW);
      }
    }
  }
}
