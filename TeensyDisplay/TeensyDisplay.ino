#include <OctoWS2811.h>

#define LED_WIDTH    90
#define LED_HEIGHT   20
#define LEDS_PER_STRIP 360
#define CONFIG       WS2811_800kHz | WS2811_GRB
#define FRAME_RATE   30

const int numPixels = LED_WIDTH * LED_HEIGHT;

DMAMEM int displayMemory[LEDS_PER_STRIP*6];
int drawingMemory[LEDS_PER_STRIP*6];

OctoWS2811 leds(LEDS_PER_STRIP, displayMemory, drawingMemory, CONFIG);

void setup() {
  Serial.setTimeout(50);
  leds.begin();
  leds.show();
}

void loop() {
  char messageType = Serial.read();
  
  if (messageType == '?') {
    // print config
    Serial.print(LED_WIDTH);
    Serial.print(",");
    Serial.print(LED_HEIGHT);
    Serial.println();
  } else if (messageType == '*') {
    // receive a frame
    int x, y, address, pixel = 0;
    for (int i = 0; i < numPixels; i++) {
      x = i % LED_WIDTH;
      y = i / LED_WIDTH;
      
      if (y % 2 == 0) {
        address = i;
      } else {
        address = y * LED_WIDTH + LED_WIDTH - x - 1;
      }

      Serial.readBytes((char*)&pixel, 3);
      // reverse BGR -> RGB
      pixel = (0x000000ff & pixel) << 16 
            | (0x0000ff00 & pixel) 
            | (0x00ff0000 & pixel) >> 16;
        
      leds.setPixel(address, pixel);
    }
  } else {
    // swallow garbage
  }
  leds.show();
}
