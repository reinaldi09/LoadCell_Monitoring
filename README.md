# LoadCell_Monitoring
This project monitors load cell data using an ESP32, transmitting readings to a Python server via WiFi. Data is stored in a SQLite database and displayed on a real-time web interface. Features include real-time acquisition, wireless communication, data storage, web interface, and data export in CSV format.

# ESP32 Load Cell Data Monitoring

This project demonstrates a complete system for monitoring load cell data using an ESP32 microcontroller. The system reads data from three load cells, transmits the data to a Python-based server, stores the data in a SQLite database, and displays real-time monitoring results on a web interface.

## Features

- **Real-time Data Acquisition:** Utilizes an ESP32 to read data from three load cells simultaneously.
- **Wireless Communication:** Sends load cell data to a server over WiFi.
- **Data Storage:** Saves received data in a SQLite database for persistent storage.
- **Web Interface:** Provides a user-friendly web interface to display real-time load cell readings.
- **Data Export:** Allows users to download the recorded data in CSV format.

## Components

1. **ESP32 Microcontroller:**
   - Connects to WiFi and reads data from three load cells.
   - Transmits data to the server using HTTP POST requests.

2. **Python Server:**
   - Built with Flask to handle incoming data from the ESP32.
   - Stores data in a SQLite database.
   - Serves a web page to display real-time data.

3. **Web Interface:**
   - Built with HTML to display the latest load cell readings.
   - Provides an endpoint to download the data as a CSV file.

## Installation

### ESP32 Setup

1. Install the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
2. Install the necessary libraries: `WiFi`, `HX711`, and `HTTPClient`.
3. Copy the ESP32 code from the [ESP32 Code](#esp32-code) section and upload it to your ESP32.
4. Update the WiFi credentials and server URL in the code.

### Python Setup

1. Ensure you have Python 3 installed.
2. Install the required libraries:
    ```bash
    pip install flask flask-cors
    ```
3. Create the SQLite database and table:
    ```sql
    CREATE TABLE sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        loadcell1 REAL NOT NULL,
        loadcell2 REAL NOT NULL,
        loadcell3 REAL NOT NULL
    );
    ```
4. Run the Python script:
    ```bash
    python app.py
    ```
5. Access the web interface by navigating to `http://<your_server_ip>:5000` in your browser.

## Usage

### ESP32 Code

The ESP32 code initializes the WiFi connection, reads data from the load cells, converts the readings to JSON format, and sends the data to the server.

### Python Code

The Python script sets up a Flask server to receive data from the ESP32, saves the data in a SQLite database, and serves a web page to display the data. It also provides an endpoint to download the data as a CSV file.

### Web Interface

The web interface displays the latest load cell readings and allows users to download the data in CSV format.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.
   
### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
If you have any questions or suggestions, please feel free to contact me.



## ESP32 Code

```cpp
#include <WiFi.h>
#include <HX711.h>
#include <HTTPClient.h>

// WiFi credentials
const char* ssid = "Your_SSID";
const char* password = "Your_PASSWORD";

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
const char* server_url = "http://<your_server_ip>:5000/upload";

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

void loop() {
  if (scale1.is_ready() && scale2.is_ready() && scale3.is_ready()) {
    // Read the load cell data
    long reading1 = scale1.read();
    long reading2 = scale2.read();
    long reading3 = scale3.read();
    
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


