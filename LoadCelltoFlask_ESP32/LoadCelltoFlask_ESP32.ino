#include <WiFi.h>
#include <HX711.h>
#include <HTTPClient.h>

// WiFi credentials
const char* ssid = "Virnia";
const char* password = "17121998";

// HX711 pins
const int LOADCELL1_DOUT_PIN = 16;
const int LOADCELL1_SCK_PIN = 4;
const int LOADCELL2_DOUT_PIN = 17;
const int LOADCELL2_SCK_PIN = 5;
const int LOADCELL3_DOUT_PIN = 18;
const int LOADCELL3_SCK_PIN = 6;

// HX711 objects
HX711 scale1;
HX711 scale2;
HX711 scale3;

// Server URL
const char* server_url = "http://192.168.1.4:5000/upload";  // Replace with your server URL

void setup() {
  Serial.begin(115200);
  delay(10);

  // Initialize WiFi
  Serial.println();
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected.");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Initialize the load cells
  scale1.begin(LOADCELL1_DOUT_PIN, LOADCELL1_SCK_PIN);
  scale2.begin(LOADCELL2_DOUT_PIN, LOADCELL2_SCK_PIN);
  scale3.begin(LOADCELL3_DOUT_PIN, LOADCELL3_SCK_PIN);
}

//void loop() {
//  if (scale1.is_ready() && scale2.is_ready() && scale3.is_ready()) {
//    // Read the load cell data
//    long reading1 = scale1.read();
//    long reading2 = scale2.read();
//    long reading3 = scale3.read();
//    
//    Serial.print("Load cell 1 reading: ");
//    Serial.println(reading1);
//    Serial.print("Load cell 2 reading: ");
//    Serial.println(reading2);
//    Serial.print("Load cell 3 reading: ");
//    Serial.println(reading3);
//
//    // Convert the readings to JSON
//    String jsonData = "{\"loadcell1\":" + String(reading1) + ",\"loadcell2\":" + String(reading2) + ",\"loadcell3\":" + String(reading3) + "}";
//
//    // Send the data to the server
//    if (WiFi.status() == WL_CONNECTED) {
//      HTTPClient http;
//      http.begin(server_url);
//      http.addHeader("Content-Type", "application/json");
//
//      int httpResponseCode = http.POST(jsonData);
//      if (httpResponseCode > 0) {
//        String response = http.getString();
//        Serial.print("POST response code: ");
//        Serial.println(httpResponseCode);
//        Serial.println(response);
//      } else {
//        Serial.print("Error sending data: ");
//        Serial.println(httpResponseCode);
//      }
//      http.end();
//    } else {
//      Serial.println("WiFi not connected");
//    }
//  } else {
//    Serial.println("One or more HX711 not found.");
//  }
//
//  // Wait before the next reading
//  delay(1000);  // Adjust the delay as needed
//}

void loop() {
  if (scale1.is_ready()) {
    // Read the load cell data
    long reading1 = scale1.read();
    long reading2 = random(1000, 5000); 
    long reading3 = random(1000, 5000); 
    
    Serial.print("Load cell 1 reading: ");
    Serial.println(reading1);
    Serial.print("Load cell 2 reading: ");
    Serial.println(reading2);
    Serial.print("Load cell 3 reading: ");
    Serial.println(reading3);

    // Convert the readings to JSON
    String jsonData = "{\"loadcell1\":" + String(reading1) + ",\"loadcell2\":" + String(reading2) + ",\"loadcell3\":" + String(reading3) + "}";

    // Send the data to the server
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(server_url);
      http.addHeader("Content-Type", "application/json");

      int httpResponseCode = http.POST(jsonData);
      if (httpResponseCode > 0) {
        String response = http.getString();
        Serial.print("POST response code: ");
        Serial.println(httpResponseCode);
        Serial.println(response);
      } else {
        Serial.print("Error sending data: ");
        Serial.println(httpResponseCode);
      }
      http.end();
    } else {
      Serial.println("WiFi not connected");
    }
  } else {
    Serial.println("One or more HX711 not found.");
  }

  // Wait before the next reading
  delay(1000);  // Adjust the delay as needed
}
