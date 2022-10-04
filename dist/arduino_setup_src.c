/* Generated User Define with UnoGenerator */
#define DIGITAL_PIN_2 2
#define DIGITAL_PIN_3 3
#define DIGITAL_PIN_6 6
#define ANALOG_PIN_A3 A3
/* User Define End */

void setup() {
/* Generated User Pin Initialize with UnoGenerator */
  pinMode(DIGITAL_PIN_2, INPUT);
  pinMode(ANALOG_PIN_A3, INPUT);

  pinMode(DIGITAL_PIN_3, OUTPUT);
  pinMode(DIGITAL_PIN_6, OUTPUT);
/* User Pin Initialize End */

}

void loop() {
/* Generated Example Code with UnoGenerator */
  val0 = digitalRead(DIGITAL_PIN_2)
  val1 = analogRead(ANALOG_PIN_A3)

  analogWrite(DIGITAL_PIN_3, 100)
  digitalWrite(DIGITAL_PIN_6, HIGH)
/* Example Code End */

}
