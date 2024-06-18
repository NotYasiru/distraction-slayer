void setup() {
	Serial.begin(9600); 
	Serial.setTimeout(1); 
  	pinMode(7, OUTPUT);
} 
void loop() {
	while (!Serial.available()); 
	int x = Serial.readString().toInt();
  	if(x == 2){
		digitalWrite(7, HIGH);
	}
  	else if(x == 1){
		digitalWrite(7, LOW);
	}
}
