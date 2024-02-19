// include the library code:
#include <LiquidCrystal.h>
#include <DHT11.h>

DHT11 dht11(46);
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN
const byte address[6] = "00001";
// Creates an LCD object. Parameters: (rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() 
{
	// set up the LCD's number of columns and rows:
	lcd.begin(16, 2);
	// Clears the LCD screen
	lcd.clear();

  radio.begin();
  radio.setChannel(0x76); // It's important to use the same channel for both Arduino and Raspberry Pi
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MAX);
  radio.enableDynamicPayloads(); // Enable dynamic payloads
  radio.enableAckPayload(); // Optional: Enable payload with ACK
  radio.stopListening();
}

void loop() 
{
  int temperature = dht11.readTemperature();

    // Check the result of the reading.
    // If there's no error, print the temperature value.
    // If there's an error, print the appropriate error message.
    if (temperature != DHT11::ERROR_CHECKSUM && temperature != DHT11::ERROR_TIMEOUT)
    {
        Serial.print("Temperature: ");
        Serial.print(temperature);
        Serial.println(" °C");
    }
    else
    {
        Serial.println(DHT11::getErrorString(temperature));
    }
	// Print a message to the LCD.
  lcd.setCursor(0, 0);
	lcd.print("Temperature: ");

	// set the cursor to column 0, line 1
	// (note: line 1 is the second row, since counting begins with 0):
	lcd.setCursor(0, 1);
	// Print a message to the LCD.
	lcd.print(temperature);

  int temp = temperature;  // Example temperature
  radio.write(&temp, sizeof(temp));
 
  delay(1000);
}