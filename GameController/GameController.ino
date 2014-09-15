
// button input pins
#define BTN_P1_BLUE    34
#define BTN_P1_RED     32
#define BTN_P1_YELLOW  30
#define BTN_P1_UP      28
#define BTN_P1_DOWN    24
#define BTN_P1_LEFT    26
#define BTN_P1_RIGHT   22

#define BTN_P2_BLUE    40
#define BTN_P2_RED     38
#define BTN_P2_YELLOW  36
#define BTN_P2_UP      48
#define BTN_P2_DOWN    44
#define BTN_P2_LEFT    46
#define BTN_P2_RIGHT   42

const byte buttons[] = {
  BTN_P1_BLUE, BTN_P1_RED, BTN_P1_YELLOW, BTN_P1_UP, BTN_P1_DOWN, BTN_P1_LEFT, BTN_P1_RIGHT,
  BTN_P2_BLUE, BTN_P2_RED, BTN_P2_YELLOW, BTN_P2_UP, BTN_P2_DOWN, BTN_P2_LEFT, BTN_P2_RIGHT
};
const int buttonCount = 14;
byte buttonStates[buttonCount] = {0};
unsigned long lastTime = 0;
const long debounce = 20;

void setup() {
 Serial.begin(115200);
 for (int i = 0; i < buttonCount; i++) {
    pinMode(buttons[i], INPUT);
 }
}

void loop() {
  if(millis()-lastTime>debounce)
  {
      byte value = 0;
      for (int i = 0; i < buttonCount; i++) {
        value = digitalRead(buttons[i]);
        if (value != buttonStates[i]) {
          send(buttons[i], value);
          buttonStates[i] = value;
        }
     }
     lastTime = millis();
  }
}

void send(byte button, byte val)
{
  Serial.write(button | val);
  Serial.flush();
} 
