#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_BMP085.h>

// Pines del sensor de ultrasonidos
#define trigPin 5 // D1
#define echoPin 4 // D2

// Pin diodo led
#define ledPin 2 //D4

// Pines sda y scl para la pantalla y el sensor de temperatura
#define sdaPin 13 // D7
#define sclPin 12 // D6

Adafruit_SSD1306 display(128, 64, &Wire, -1); // definicion del display de la pantalla OLED
Adafruit_BMP085 bmp;                          // definicion del sensor bmp

/********************************************************/

void setup() {
  Serial.begin(9600);

  pinMode ( ledPin, OUTPUT );
  pinMode ( trigPin, OUTPUT );
  pinMode(echoPin, INPUT);
  digitalWrite(trigPin, LOW);
  digitalWrite(ledPin, LOW);

  Wire.begin(sdaPin, sclPin); 
  
  // Inicializar el sensor BMP180
  if (!bmp.begin()) {
    Serial.println("No se pudo encontrar el sensor BMP180");
    while (true);
  }

  //Inicializar la pantalla OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("No se pudo iniciar la pantalla OLED"));
    while (true);
  }
  display.clearDisplay();  
}

void loop() {
  delay(1000);
  
  // Medida de la distancia
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  float distancia = 0.0172*pulseIn(echoPin, HIGH);
  
  // Activacion del LED
  int led = distancia < 10 ? 1 : 0;  // 0=desactivado, 1=activado 
  digitalWrite(ledPin, led);  

  // Leer temperatura y la presion del BMP180
  float temperature = bmp.readTemperature();
  int32_t pressure = bmp.readPressure();

  // Mostrar los datos en la pantalla OLED
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.print(distancia);
  display.print(" cm");
  display.setCursor(0, 25);
  display.print(temperature);
  display.println(" C");
  display.setCursor(0, 50); 
  display.print(pressure / 100.0);
  display.println(" hPa");
  display.display();

  // Visualización por el puerto serie
  Serial.print("Distancia: ");
  Serial.println(distancia);
  Serial.print(" Temperatura: ");
  Serial.println(temperature);
  Serial.print(" Presion: ");
  Serial.println(pressure / 100.0);
}