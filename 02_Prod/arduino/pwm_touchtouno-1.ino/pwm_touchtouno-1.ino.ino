const int pwmPin =  9; // Remplacez par le numéro de broche PWM de votre Arduino


void setup() {
  Serial.begin(9600); // Assurez-vous que cela correspond au baud rate de TouchDesigner
  pinMode(pwmPin, OUTPUT); 
}

void loop() {
  if (Serial.available()) {
    int pwmValue = Serial.parseInt();
    analogWrite(pwmPin, pwmValue);
  }
}
