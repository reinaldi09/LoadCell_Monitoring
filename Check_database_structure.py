import sqlite3

conn = sqlite3.connect('sensordata.db')
cursor = conn.cursor()

# Get table structure (or use a tool like sqlitebrowser)
cursor.execute('PRAGMA table_info(sensor_data)')
table_info = cursor.fetchall()

print("Table Structure:")
for column in table_info:
  print(column[1])  # Print column names (index 1)

conn.close()
