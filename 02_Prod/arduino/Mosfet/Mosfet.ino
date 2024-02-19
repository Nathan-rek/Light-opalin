const int ledPin =  3; // Pin connected to the LED
int brightness =  0; // Initial brightness level
int fadeAmount =  5; // Amount to change the brightness by

void setup() {
  pinMode(ledPin, OUTPUT); // Set the LED pin as output
}

void loop() {
  analogWrite(ledPin, brightness); // Write the current brightness to the LED

  brightness = brightness + fadeAmount; // Change the brightness for the next iteration

  // Reverse the direction of the fading at the ends of the fade
  if (brightness <= 0  || brightness >=  255) {
    fadeAmount = -fadeAmount;
  }

  delay(100); // Wait for  100 ms before the next update
}
