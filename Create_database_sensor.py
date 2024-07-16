import sqlite3

conn = sqlite3.connect('sensordata.db')  # Replace with your filename
cursor = conn.cursor()

# Create the table (modify column names and data types if needed)
sql = '''CREATE TABLE IF NOT EXISTS sensor_data (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT NOT NULL,
              time TEXT NOT NULL,
              loadcell1 REAL NOT NULL,
              loadcell2 INTEGER NOT NULL,
              loadcell3 INTEGER NOT NULL
           )'''
cursor.execute(sql)
conn.commit()
conn.close()

print("Table 'sensor_data' created successfully!")

# timestamp DATETIME NOT NULL,