/* Generated User Define with UnoGenerator */
#define BUTTON 5
#define BUTTON2 6
#define LED1 10
#define BUZZER 11
#define LED2 A2
#define SENSOR A3
/* User Define End */

void setup() {
/* Generated User Pin Initialize with UnoGenerator */
  pinMode(BUTTON, INPUT);
  pinMode(BUTTON2, INPUT);
  pinMode(SENSOR, INPUT);

  pinMode(LED1, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(LED2, OUTPUT);
/* User Pin Initialize End */

}

void loop() {
/* Generated Example Code with UnoGenerator */
  val0 = digitalRead(BUTTON)
  val1 = digitalRead(BUTTON2)
  val2 = analogRead(SENSOR)

  digitalWrite(LED1, HIGH)
  analogWrite(BUZZER, 100)
  digitalWrite(LED2, HIGH)
/* Example Code End */

}
