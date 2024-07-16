from flask import Flask, request, render_template, make_response, jsonify
from flask_cors import CORS
import sqlite3
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Variables to store the latest sensor readings
latest_loadcell1 = None
latest_loadcell2 = None
latest_loadcell3 = None

def connect_db():
    conn = sqlite3.connect('sensordata.db')
    return conn

def save_sensor_data(data):
    conn = connect_db()
    cursor = conn.cursor()
    if not isinstance(data, dict) or "loadcell1" not in data or "loadcell2" not in data or "loadcell3" not in data:
        conn.close()
        return
    sql = "INSERT INTO sensor_data (date, time, loadcell1, loadcell2, loadcell3) VALUES (?, ?, ?, ?, ?)"
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    loadcell1 = data["loadcell1"]
    loadcell2 = data["loadcell2"]
    loadcell3 = data["loadcell3"]
    try:
        cursor.execute(sql, (date, time, loadcell1, loadcell2, loadcell3))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error saving data: {e}")
    finally:
        conn.close()

@app.route("/", methods=["GET"])
def show_data():
    global latest_loadcell1, latest_loadcell2, latest_loadcell3
    return render_template("index.html", loadcell1=latest_loadcell1, loadcell2=latest_loadcell2, loadcell3=latest_loadcell3)

@app.route("/upload", methods=["POST"])
def upload_data():
    global latest_loadcell1, latest_loadcell2, latest_loadcell3
    if request.is_json:
        data = request.get_json()
        latest_loadcell1 = data.get("loadcell1")
        latest_loadcell2 = data.get("loadcell2")
        latest_loadcell3 = data.get("loadcell3")
        save_sensor_data(data)
        return jsonify({"message": "Data received and saved successfully!"}), 200
    else:
        return jsonify({"message": "Invalid data format!"}), 400

@app.route("/download", methods=["GET"])
def download_data():
    conn = connect_db()
    cursor = conn.cursor()
    sql = "SELECT * FROM sensor_data"
    cursor.execute(sql)
    data = cursor.fetchall()
    csv_data = "id,date,time,loadcell1,loadcell2,loadcell3\n"
    for row in data:
        csv_data += ",".join([str(x) for x in row]) + "\n"
    response = make_response(csv_data)
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    response.headers["Content-Disposition"] = "attachment; filename=sensor_data.csv"
    conn.close()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')