/* Generated User Define with UnoGenerator */
#define DIGITAL_PIN_5 5
#define DIGITAL_PIN_10 10
#define ANALOG_PIN_A2 A2
#define ANALOG_PIN_A3 A3
/* User Define End */

void setup() {
/* Generated User Pin Initialize with UnoGenerator */
  pinMode(DIGITAL_PIN_5, INPUT);
  pinMode(ANALOG_PIN_A3, INPUT);

  pinMode(DIGITAL_PIN_10, OUTPUT);
  pinMode(ANALOG_PIN_A2, OUTPUT);
/* User Pin Initialize End */

}

void loop() {
/* Generated Example Code with UnoGenerator */
  int val0 = digitalRead(DIGITAL_PIN_5);
  int val1 = analogRead(ANALOG_PIN_A3);

  digitalWrite(DIGITAL_PIN_10, HIGH);
  digitalWrite(ANALOG_PIN_A2, HIGH);
/* Example Code End */

}
