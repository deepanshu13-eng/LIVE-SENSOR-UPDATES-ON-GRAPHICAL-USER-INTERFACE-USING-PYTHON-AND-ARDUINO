int pinDHT11 = 8;                          // Initializing DHT-11 sensor pin number. 
#include <SimpleDHT.h>                     // Including DHT-11 sensor library. You can find this library on Github. 
SimpleDHT11 dht11(pinDHT11);               
int sensorValue = 0;                       // Declaring sensorval as integer and initializing it to zero in starting.
int percentvalue = 0;                      // Declaring percentvalue as integer and initializing it equal to zero.

int sensorPin = A0;                        // Initializing Soil Moisture Sensor to A0.



void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);                        // Setting up Serial rate at 9600 byts per second.

}

void loop() {
  // put your main code here, to run repeatedly:
byte temperature = 0;                                // Declaring a byte called temperature and Initializing a value to it.
byte humidity = 0;                                   // Declaring a byte called humidity and Initializing a value to it.
int err;                                             // Declaring err as an integer.
sensorValue = analogRead(sensorPin);                 // Reading analog values from soil moisture sensor and storing it to sensorValue.
percentvalue = map(sensorValue, 1023, 200, 0, 100);  // Mapping sensorValue between 1023 and 200 to 0 to 100. 


err = dht11.read(&temperature, &humidity, NULL);  // Reading the DHT-1 sensor values.

// Temperature Values

Serial.print("\nTemperature:");                   // Printing Temperature on serial. Python will check for this word first and then it will print the temperature value on GUI.
Serial.print((int)temperature);                   // Printing temperature values on serial.
Serial.print("*C");                               // printing "*C" on serial.

//  Humidity Values

Serial.print("\nHumidity:");                      // Printing Humidity on serial. Python will check for this word first and then print the humidity value on GUI.  
Serial.print((int)humidity);                      // Printing humidity value on serial.
Serial.print("%");                                // Printing "%" on serial. 

// Soil Moisture Values

Serial.print("\nPercentvalue:");                  // Printing Percentvalue on serial. Python will check for this word first and the print the Percentvalue of Soil Moisture value on GUI.
Serial.print((int)percentvalue);                  // Printing values of percentvalue on serial.
Serial.print("%");                                // Printing "%" on serial.

delay(1000);                                      // Giving a delay time of 1 second.
}
