int LED =  60;
int state =  0;

int button = 4;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);

  pinMode(LED, OUTPUT);
  pinMode(button, INPUT);
}

void loop () {

  if(Serial.available() >  0) 
  {
    int temp = Serial.parseInt();
  }

if (CirclePlayground.mic.soundPressurLevel(10) > 100)
  state = 1;
if(digitalRead(button) == HIGH)
  state = 1;

   
  if(state ==  0) 
  {
    digitalWrite(LED, LOW);

  } 
  else 
  {
    digitalWrite(LED, HIGH);
  }

}
