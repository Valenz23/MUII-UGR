#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <WiFiClient.h>
#include "mqtt_secrets.h"
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_BMP085.h>
#include <WiFiClientSecure.h>

// Pines del sensor de ultrasonidos
#define trigPin 5 // D1
#define echoPin 4 // D2

// Pin diodo led
#define ledPin 2 //D4

// Pines sda y scl para la pantalla y el sensor de temperatura
#define sdaPin 13 // D7
#define sclPin 12 // D6

Adafruit_SSD1306 display(128, 64, &Wire, -1); // definicion del display de la pantalla OLED
Adafruit_BMP085 bmp;    

// Configuración de Wifi
char ssid[] = "PablOno2";
char pass[] = "basKET,2:N";

/* Setup de ThingSpeak */
const char* publish_ts = "channels/2550878/publish"; 
const char* mqtt_server_ts = "mqtt3.thingspeak.com";

const char* f1_ts = "channels/2550878/subscribe/fields/field1"; 
const char* f2_ts = "channels/2550878/subscribe/fields/field2"; 
const char* f3_ts = "channels/2550878/subscribe/fields/field3"; 
const char* f4_ts = "channels/2550878/subscribe/fields/field4"; 

WiFiClient espClient_ts;
PubSubClient client_ts(espClient_ts);

/* Setup de HiveMQ*/
const char* mqtt_server_hv = "broker.hivemq.com";
const char* f1_hv = "telemetroPLUS/distancia";
const char* f2_hv = "telemetroPLUS/temperatura";
const char* f3_hv = "telemetroPLUS/presion";
const char* f4_hv = "telemetroPLUS/led";

WiFiClient espClient_hv;
PubSubClient client_hv(espClient_hv); 

//////////////////////////////////////////////////////////////////

const unsigned long postingInterval = 20L * 1000L; 
unsigned long lastUploadedTime = 0;

/* funciones */

// Conexión de WiFi
void setup_wifi(){    
  delay(10);
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi conectado");
}

// reconectar cliente mqtt de thingspeak
void reconnect_ts() {
  while (!client_ts.connected()) {
    Serial.print("Intentando la conexión MQTT a ");
    Serial.print(mqtt_server_ts);
    Serial.println(" ...");
    if (client_ts.connect(SECRET_MQTT_CLIENT_ID, SECRET_MQTT_USERNAME, SECRET_MQTT_PASSWORD)) {  
      Serial.println("conectado");
      client_ts.subscribe(f1_ts);  
      client_ts.subscribe(f2_ts);
      client_ts.subscribe(f3_ts);
      client_ts.subscribe(f4_ts);
      
    } else {
      Serial.print("fallo, rc=");
      Serial.print(client_ts.state());
      Serial.println(" intentando de nuevo en 5 segundos");   
      delay(5000);
    }
  }
}

void reconnect_hv() {
  while (!client_hv.connected()) {
    Serial.print("Intentando la conexión MQTT a ");
    Serial.print(mqtt_server_hv);
    Serial.println(" ...");
    if (client_hv.connect("telemetroPLUS")) {  
      Serial.println("conectado");       
      client_hv.subscribe(f1_hv);
      client_hv.subscribe(f2_hv);
      client_hv.subscribe(f3_hv);
      client_hv.subscribe(f4_hv); 
    } else {
      Serial.print("fallo, rc=");
      Serial.print(client_hv.state());
      Serial.println(" intentando de nuevo en 5 segundos");   
      delay(5000);
    }
  }
}

/**************************************/
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

  setup_wifi();
  client_ts.setServer(mqtt_server_ts, 1883);

  // espClient_hv.setInsecure();
  client_hv.setServer(mqtt_server_hv, 1883);
}

void loop() {

  // comprobacion de la conexión a ThingSpeak
  if (!client_ts.connected()) reconnect_ts();

  // comprobacion de la conexión a HiveMQ
  if (!client_hv.connected()) reconnect_hv();

  client_ts.loop();

  // Envío datos cada 20 segundos
  if(millis() - lastUploadedTime > postingInterval){

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
    Serial.print(" LED: ");
    Serial.println(led); 
      
    // Envio a ThingSpeak
    String topics = String("field1=" + String(distancia) + "&field2=" + String(temperature) + "&field3=" + String(pressure / 100.0) + "&field4=" + String(led) + "&status=MQTTPUBLISH");
    if (client_ts.publish(publish_ts, topics.c_str())) Serial.println("Datos enviados a ThingSpeak");
    else Serial.println("Error al enviar los datos");

    //Envío a HiveMQ
    if (client_hv.publish(f1_hv, String(distancia).c_str()) &&
        client_hv.publish(f2_hv, String(temperature).c_str()) &&
        client_hv.publish(f3_hv, String(pressure/100).c_str()) &&
        client_hv.publish(f4_hv, String(led).c_str())) {
      Serial.println("Datos enviados a HiveMQ");
    } else Serial.println("Error al enviar los datos");

    lastUploadedTime = millis();
  }

}
