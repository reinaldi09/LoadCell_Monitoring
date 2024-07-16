# LoadCell_Monitoring
### Short Description
This project monitors load cell data using an ESP32, transmitting readings to a Python server via WiFi. Data is stored in a SQLite database and displayed on a real-time web interface. Features include real-time acquisition, wireless communication, data storage, web interface, and data export in CSV format.

## Table of Contents
- [Description](#loadcell_monitoring)
- [Features](#features)
- [Components](#components)
- [Installation](#installation)
  - [ESP32 Setup](#esp32-setup)
  - [Python Setup](#python-setup)
- [Usage](#usage)
  - [ESP32 Code](#esp32-code)
  - [Python Code](#python-code)
  - [Web Interface](#web-interface)
- [Contributing](#contributing)
- [License](#license)

# ESP32 Load Cell Data Monitoring - DESCRIPTION

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
    Run the Python script:
    ```bash
    python Create_database_sensor.py
    ```
    
4. Run the Python script:
    ```bash
    python main.py
    ```

    and this script to simulate sending data to flask.
    ```bash
    Test_send_data_to_flask.py
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


aaaaaa