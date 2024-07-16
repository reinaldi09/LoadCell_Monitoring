import requests
import json
import time
import random

server_url = "http://127.0.0.1:5000/upload"  # Replace with your server URL if different

def simulate_loadcell_data():
    # Generate some simulated load cell data
    data = {
        "loadcell1": random.randint(20.0, 300.0), # Replace with your simulated load cell reading
        "loadcell2": random.randint(35.0, 70.0),  # Replace with your simulated load cell reading
        "loadcell3": random.randint(70.0, 100.0)
    }
    return data

while True:
    data = simulate_loadcell_data()
    response = requests.post(server_url, json=data)
    if response.status_code == 200:
        print("Data sent successfully:", data)
    else:
        print("Failed to send data:", response.status_code, response.text)
    time.sleep(5)  # Wait 5 seconds before sending the next data point
